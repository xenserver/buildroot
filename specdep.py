#!/usr/bin/python

# see http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch16s04.html

import sys
import glob
import os
import platform
import rpm
import urlparse

from scripts.lib import mappkgname


IGNORE_LIST = {"rpm":["libnl3"],
               "deb":["libnl3"]}


def build_type():
    debian_like = ["ubuntu", "debian"]
    rhel_like = ["fedora", "redhat", "centos"]

    dist = platform.linux_distribution(full_distribution_name=False)[0].lower()
    assert dist in debian_like + rhel_like

    if dist in debian_like:
        return "deb"
    elif dist in rhel_like:
        return "rpm"


def map_package_name(name):
    if build_type() == "rpm":
        return [name]
    else:
        return mappkgname.map_package(name)


# for debugging, make all paths relative to PWD
rpm.addMacro('_topdir', '.')

# Directories where rpmbuild/mock expects to find inputs
# and writes outputs
RPMDIR = rpm.expandMacro('%_rpmdir')
SPECDIR = rpm.expandMacro('%_specdir')
SRPMDIR = rpm.expandMacro('%_srcrpmdir')
SRCDIR = rpm.expandMacro('%_sourcedir')


# Some RPMs include the value of '%dist' in the release part of the
# filename.   In the mock chroot, %dist is set to a CentOS release
# such as '.el6', so RPMs produced by mock will have that in their
# names.   However if we generate the dependencies in a Fedora 'host',
# the filenames will be generated with a %dist of '.fc18' instead.
# We need to override %dist with the value from the chroot so these 
# dependencies are named correctly.

# The same problem occurs with rpmbuild.   We currently run rpmbuild on
# the host to build SRPMs.   By default it will use the host's %dist value
# when naming the SRPM.   This won't match the patterns in the Makefile,
# so we need to make sure that, whenever we run rpmbuild, we also override
# %dist (on the command line) to have the same value as the chroot.

# We could avoid hardcoding this by running 
# "mock -r xenserver --chroot "rpm --eval '%dist'"
CHROOT_DIST = '.el6'
if build_type() == "rpm":
    rpm.addMacro('dist', CHROOT_DIST)
else:
    rpm.addMacro('dist', "")


if build_type() == "rpm":
    RPMFILENAMEPAT = rpm.expandMacro('%_build_name_fmt')
else:
    RPMFILENAMEPAT = "%{NAME}_%{VERSION}-%{RELEASE}_%{ARCH}.deb"


def spec_from_file(spec):
    try:
        return rpm.ts().parseSpec(spec)
    except Exception, exn:
        print >> sys.stderr, "Failed to parse %s" % spec
        raise exn


def srpm_name_from_spec(spec):
    hdr = spec.sourceHeader
    rpm.addMacro('NAME', map_package_name(hdr['name'])[0])
    rpm.addMacro('VERSION', hdr['version'])
    rpm.addMacro('RELEASE', hdr['release'])
    rpm.addMacro('ARCH', 'src')

    # There doesn't seem to be a macro for the name of the source
    # rpm, but the name appears to be the same as the rpm name format.
    # Unfortunately expanding that macro gives us a leading 'src' that we
    # don't want, so we strip that off

    if build_type() == "rpm":
        srpmname = os.path.basename(rpm.expandMacro(RPMFILENAMEPAT))  
    else:
        srpmname = os.path.basename(
            rpm.expandMacro("%{NAME}_%{VERSION}-%{RELEASE}.dsc"))

    rpm.delMacro('NAME')
    rpm.delMacro('VERSION')
    rpm.delMacro('RELEASE')
    rpm.delMacro('ARCH')

    return srpmname


def rpm_names_from_spec(spec):
    def rpm_name_from_header(hdr):
        rpm.addMacro('NAME', map_package_name(hdr['name'])[0])
        rpm.addMacro('VERSION', hdr['version'])
        rpm.addMacro('RELEASE', hdr['release'])
        if build_type() == "rpm":
            rpm.addMacro('ARCH', hdr['arch'])
        else:
            rpm.addMacro(
                'ARCH', "amd64" if hdr['arch'] == "x86_64" 
                else "all" if hdr['arch'] == "noarch" 
                else hdr['arch'])
        rpmname = rpm.expandMacro(RPMFILENAMEPAT)
        rpm.delMacro('NAME')
        rpm.delMacro('VERSION')
        rpm.delMacro('RELEASE')
        rpm.delMacro('ARCH')
        return rpmname
    return [rpm_name_from_header(pkg.header) for pkg in spec.packages]


# Rules to build SRPM from SPEC
def build_srpm_from_spec(spec, specname):
    srpmname = srpm_name_from_spec(spec)

    # spec.sourceHeader['sources'] and ['patches'] doesn't work 
    # in RPM 4.8 on CentOS 6.4.   spec.sources contains both
    # sources and patches, but with full paths which must be
    # chopped.
    sources = []
    for (source, _, _) in spec.sources:
        url = urlparse.urlparse(source)

        # Source comes from a remote HTTP server
        if url.scheme in ["http", "https"]:
            sources.append(os.path.join(SRCDIR, os.path.basename(url.path)))

        # Source comes from a local file or directory
        if url.scheme == "file":
            sources.append(
                os.path.join(SRCDIR, os.path.basename(url.fragment)))

        # Source is an otherwise unqualified file, probably a patch
        if url.scheme == "":
            sources.append(os.path.join(SRCDIR, url.path))

    print '%s: %s %s' % (os.path.join(SRPMDIR, srpmname), 
                         os.path.join(SPECDIR, specname),
                         " ".join(sources))
    if build_type() == "rpm":
        print '\t@echo [RPMBUILD] $@' 
        print '\t@rpmbuild --quiet --define "_topdir ." --define "%%dist %s" -bs $<' % CHROOT_DIST
    else:
        print '\t@echo [MAKEDEB] $@'
        print '\tscripts/deb/makedeb.py $<'


# Rules to download sources

# Assumes each RPM only needs one download - we have some multi-source
# packages but in all cases the additional sources are patches provided
# in the Git repository
def download_rpm_sources(spec, specname):
    # The RPM documentation says that RPM only cares about the basename
    # of the path given in a Source: tag.   spec.sourceHeader['url'] 
    # enforces this - even if we have a URL in the source tag, it 
    # will only give us the basename.   However the full tag text is
    # available in spec.sources.   It's not clear whether or not we
    # can rely on this as part of the RPM library API.

    for (source, _, _) in spec.sources:
        url = urlparse.urlparse(source)

        # Source comes from a remote HTTP server
        if url.scheme in ["http", "https"]:
            print '%s: %s' % (
                os.path.join(SRCDIR, os.path.basename(url.path)),
                os.path.join(SPECDIR, specname))
            print '\t@echo [CURL] $@' 
            print '\t@curl --silent --show-error -L -o $@ %s' % source

        # Source comes from a local file or directory
        if url.scheme == "file":
            print '%s: %s $(shell find %s)' % (
                os.path.join(SRCDIR, os.path.basename(url.fragment)),
                os.path.join(SPECDIR, specname),
                url.path)

            # Assume that the directory name is already what's expected by the
            # spec file, and prefix it with the version number in the tarball
            print '\t@echo [GIT] $@'
            dirname = "%s-%s" % (os.path.basename(url.path), 
                                 spec.sourceHeader['version'])
            print '\t@git --git-dir=%s/.git '\
                'archive --prefix %s/ -o $@ HEAD' % (url.path, dirname)



# Rules to build RPMS from SRPMS (uses information from the SPECs to
# get packages)
def build_rpm_from_srpm(spec):
    # This doesn't generate the right Makefile fragment for a multi-target
    # rule - we may end up building too often, or not rebuilding correctly
    # on a partial build
    rpmnames = rpm_names_from_spec(spec)
    srpmname = srpm_name_from_spec(spec)
    for rpmname in rpmnames: 
        rpm_path = os.path.join(RPMDIR, rpmname)
        srpm_path = os.path.join(SRPMDIR, srpmname)
        rpm_outdir = os.path.dirname(rpm_path)
        print '%s: %s' % (rpm_path, srpm_path)
        if build_type() == "rpm":
            print '\t@echo [MOCK] $@'
            print '\t@mock --configdir=mock --quiet -r xenserver '\
                '--resultdir="%s" $<' % rpm_outdir
            print '\t@echo [CREATEREPO] $@'
            print '\t@createrepo --quiet --update %s' % RPMDIR

        else:
            print '\t@echo [COWBUILDER] $@'
            print '\tsudo cowbuilder --build '\
                '--configfile pbuilder/pbuilderrc-raring-amd64 '\
                '--buildresult %s $<' % rpm_outdir 


def flatten(lst):
    res = []
    for elt in lst:
        res += elt
    return res


# RPM build dependencies.   The 'requires' key for the *source* RPM is
# actually the 'buildrequires' key from the spec
def buildrequires_from_spec(spec):
    reqs = [map_package_name(r) for r in spec.sourceHeader['requires']]
    return set(flatten(reqs))

def package_to_rpm_map(specs):
    provides_to_rpm = {}
    for spec in specs:
        for package in spec.packages:
            provides = package.header['provides'] + [package.header['name']]
            for provided in set(flatten([map_package_name(r) for r in provides])):
                for rpmname in rpm_names_from_spec(spec):
                    provides_to_rpm[provided] = rpmname
    return provides_to_rpm
    

def buildrequires_for_rpm(spec, provides_to_rpm):
    for rpmname in rpm_names_from_spec(spec):
        for buildreq in buildrequires_from_spec(spec):
            # Some buildrequires come from the system repository
            if provides_to_rpm.has_key(buildreq):
                buildreqrpm = provides_to_rpm[buildreq]
                print "%s: %s" % (os.path.join(RPMDIR, rpmname), 
                                  os.path.join(RPMDIR, buildreqrpm))

def main():
    spec_paths = glob.glob(os.path.join(SPECDIR, "*.spec"))
    specs = {}

    for spec_path in spec_paths:
        spec = spec_from_file(spec_path)
        pkg_name = spec.sourceHeader['name']
        if pkg_name in IGNORE_LIST[build_type()]:
            continue
        if os.path.splitext(os.path.basename(spec_path))[0] != pkg_name:
            sys.stderr.write(
                "error: spec file name '%s' does not match package name '%s'\n" % 
                (spec_path, pkg_name))
            sys.exit(1)
            
        specs[os.path.basename(spec_path)] = spec

    provides_to_rpm = package_to_rpm_map(specs.values())
    
    print "all: rpms"

    for specname, spec in specs.iteritems():
        build_srpm_from_spec(spec, specname)
        download_rpm_sources(spec, specname)
        build_rpm_from_srpm(spec)
        buildrequires_for_rpm(spec, provides_to_rpm)
        print ""

    # Generate targets to build all srpms and all rpms
    all_rpms = []
    all_srpms = []
    for spec in specs.values():
        rpms = rpm_names_from_spec(spec)
        rpm_paths = map((lambda rpm: os.path.join(RPMDIR, rpm)), rpms)
        all_rpms += rpm_paths
        all_srpms.append(os.path.join(SRPMDIR, srpm_name_from_spec(spec)))
        print "%s: %s" % (spec.sourceHeader['name'], " ".join(rpm_paths))
    print ""
    
    print "rpms: " + " \\\n\t".join(all_rpms)
    print ""
    print "srpms: " + " \\\n\t".join(all_srpms)
    print ""
    print "install: all" 
    print "\t. scripts/%s/install.sh" % build_type()


if __name__ == "__main__":
    main()
