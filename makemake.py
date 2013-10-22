#!/usr/bin/python

# see http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch16s04.html

import sys
sys.path.append("scripts/lib")

ignore_list = {"rpm":["libxl-headers","libnl3"],
               "deb":["libnl3"]}

import rpm
import os
import urlparse
import sys
import mappkgname
import platform

def buildType():
    debian_like = [ "ubuntu", "debian" ]
    rhel_like = [ "fedora", "redhat", "centos" ]

    distribution = platform.linux_distribution()[0].lower()
    assert distribution in debian_like + rhel_like

    if distribution in debian_like:
        return "deb"
    elif distribution in rhel_like:
        return "rpm"

def map_package_name(name):
    if buildType() == "rpm":
        return [name]
    else:
        return mappkgname.map_package(name)



# for debugging, make all paths relative to PWD
rpm.addMacro( '_topdir', '.' )

# Directories where rpmbuild/mock expects to find inputs
# and writes outputs
rpm_dir = rpm.expandMacro( '%_rpmdir' )
spec_dir = rpm.expandMacro( '%_specdir' )
srpm_dir = rpm.expandMacro( '%_srcrpmdir' )
src_dir = rpm.expandMacro( '%_sourcedir' )

# Some RPMs include the value of '%dist' in the release part of the
# filename.   In the mock chroot, %dist is set to a CentOS release
# such as '.el6', so RPMs produced by mock will have that in their
# names.   However if we generate the dependencies in a Fedora 'host',
# the filenames will be generated with a %dist of '.fc18' instead.
# We can override %dist so these dependencies are named correctly,
# but we (currently) run rpmbuild directly in the host to build the
# SRPMS, so we need to make sure those dependencies use the 
# host value of %dist.   There should not be any problem with building
# the SRPMs in a distribution that is different to the one in
# which we build RPMs, as an SRPM is just a CPIO archive containing
# the spec file and the source tarball.
#
# Annoyingly, the dist interpolation is done when we read the specfile,
# so we either have to read it twice or rewrite the SRPM name appropriately.

host_dist = rpm.expandMacro( '%dist' )
# We could avoid hardcoding this by running 
# "mock -r xenserver --chroot "rpm --eval '%dist'"
chroot_dist = '.el6'
if buildType() == "rpm":
   rpm.addMacro( 'dist', chroot_dist )
else:
   rpm.addMacro( 'dist', "" )



print "all: rpms"

if buildType() == "rpm":
    rpmfilenamepat = rpm.expandMacro( '%_build_name_fmt' )
else:
    rpmfilenamepat = "%{NAME}_%{VERSION}-%{RELEASE}_%{ARCH}.deb"

ts = rpm.TransactionSet()

def specFromFile( spec ):
    try:
      return rpm.ts().parseSpec( spec )
    except Exception, e:
      print >>sys.stderr, "Failed to parse %s" % spec
      raise e

spec_names = os.listdir( spec_dir )
specs = {}
for spec_name in spec_names:
    spec = specFromFile( os.path.join( spec_dir, spec_name ) )
    pkg_name = spec.sourceHeader['name']
    if pkg_name in ignore_list[buildType()]:
        continue
    if os.path.splitext( spec_name )[0] != pkg_name:
        sys.stderr.write( "error: spec file name '%s' does not match package name '%s'\n" % ( spec_name, pkg_name ) )
        sys.exit( 1 )
        
    specs[spec_name] = spec

def srpmNameFromSpec( spec ):
    h = spec.sourceHeader
    rpm.addMacro('NAME', map_package_name(h['name'])[0])
    rpm.addMacro( 'VERSION', h['version'] )
    rpm.addMacro( 'RELEASE', h['release'] )
    rpm.addMacro( 'ARCH', 'src' )

    # There doesn't seem to be a macro for the name of the source
    # rpm, but the name appears to be the same as the rpm name format.
    # Unfortunately expanding that macro gives us a leading 'src' that we
    # don't want, so we strip that off

    if buildType() == "rpm":
        srpmname = os.path.basename( rpm.expandMacro( rpmfilenamepat ) )  
    else:
        srpmname = os.path.basename( rpm.expandMacro( "%{NAME}_%{VERSION}-%{RELEASE}.dsc" ) )  

    rpm.delMacro( 'NAME' )
    rpm.delMacro( 'VERSION' )
    rpm.delMacro( 'RELEASE' )
    rpm.delMacro( 'ARCH' )

    # HACK: rewrite %dist if it appears in the filename 
    return srpmname.replace( chroot_dist, host_dist )

def rpmNamesFromSpec( spec ):
    def rpmNameFromHeader( h ):
        rpm.addMacro('NAME', map_package_name(h['name'])[0])
        rpm.addMacro( 'VERSION', h['version'] )
        rpm.addMacro( 'RELEASE', h['release'] )
        if buildType() == "rpm":
            rpm.addMacro( 'ARCH', h['arch'] )
        else:
            rpm.addMacro( 'ARCH', "amd64" if h['arch'] == "x86_64" else "all" if h['arch'] == "noarch" else h['arch'])
        rpmname = rpm.expandMacro( rpmfilenamepat )
        rpm.delMacro( 'NAME' )
        rpm.delMacro( 'VERSION' )
        rpm.delMacro( 'RELEASE' )
        rpm.delMacro( 'ARCH' )
        return rpmname
    return [rpmNameFromHeader( p.header ) for p in spec.packages]

# Rules to build SRPM from SPEC
for specname, spec in specs.iteritems():
    srpmname = srpmNameFromSpec( spec )

    # spec.sourceHeader['sources'] and ['patches'] doesn't work 
    # in RPM 4.8 on CentOS 6.4.   spec.sources contains both
    # sources and patches, but with full paths which must be
    # chopped.
    sources = []
    for (source, _, _) in spec.sources:
        url = urlparse.urlparse( source )

        # Source comes from a remote HTTP server
        if url.scheme in ["http", "https"]:
            sources.append( os.path.join( src_dir, os.path.basename( url.path ) ) )

        # Source comes from a local file or directory
        if url.scheme == "file":
            sources.append( os.path.join( src_dir, os.path.basename( url.fragment ) ) )

        # Source is an otherwise unqualified file, probably a patch
        if url.scheme == "":
            sources.append( os.path.join( src_dir, url.path ) )

    print '%s: %s %s' % (os.path.join( srpm_dir, srpmname ), 
                         os.path.join( spec_dir, specname ),
                         " ".join( sources ) )
    if buildType() == "rpm":
        print '\t@echo [RPMBUILD] $@' 
        print '\t@rpmbuild --quiet --define "_topdir ." -bs $<'
    else:
        print '\t@echo [MAKEDEB] $@'
        print '\tscripts/deb/makedeb.py $<'

# Rules to download sources

# Assumes each RPM only needs one download - we have some multi-source
# packages but in all cases the additional sources are patches provided
# in the Git repository
for specname, spec in specs.iteritems():
    # The RPM documentation says that RPM only cares about the basename
    # of the path given in a Source: tag.   spec.sourceHeader['url'] 
    # enforces this - even if we have a URL in the source tag, it 
    # will only give us the basename.   However the full tag text is
    # available in spec.sources.   It's not clear whether or not we
    # can rely on this as part of the RPM library API.

    for (source, _, _) in spec.sources:
        url = urlparse.urlparse( source )

        # Source comes from a remote HTTP server
        if url.scheme in ["http", "https"]:
            print '%s: %s' % ( 
                os.path.join( src_dir, os.path.basename( url.path ) ),
                os.path.join( spec_dir, specname ) )
            print '\t@echo [CURL] $@' 
            print '\t@curl --silent --show-error -L -o $@ %s' % source

        # Source comes from a local file or directory
        if url.scheme == "file":
            print '%s: %s $(shell find %s)' % ( 
                os.path.join( src_dir, os.path.basename( url.fragment ) ),
                os.path.join( spec_dir, specname ),
                url.path )
            print '\t@echo [TAR] $@' 
            # assume that the directory name is already what's expected by the
            # spec file, and tag it with the version number in the tarball
            dirname = "%s-%s" % ( os.path.basename( url.path ), spec.sourceHeader['version'] )
            print '\t@tar zcf $@ -C %s --transform "s,^\./,%s/," .' % ( url.path, dirname )
    

# RPM build dependencies.   The 'requires' key for the *source* RPM is
# actually the 'buildrequires' key from the spec
def flatten(lst):
    res = []
    for li in lst:
       res += li
    return res

def buildRequiresFromSpec( spec ):
    reqs = [map_package_name(r) for r in spec.sourceHeader['requires']]
    return set(flatten(reqs))

provides_to_rpm = {}
for specname, spec in specs.iteritems():
    for package in spec.packages:
        for provided in set(flatten([map_package_name(r) for r in (package.header['provides'] + [package.header['name']])])):
            for rpmname in rpmNamesFromSpec( spec ):
                provides_to_rpm[ provided ] = rpmname

for specname, spec in specs.iteritems():
    for rpmname in rpmNamesFromSpec( spec ):
        for buildreq in buildRequiresFromSpec( spec ):
            # Some buildrequires come from the system repository
            if provides_to_rpm.has_key( buildreq ):
                buildreqrpm = provides_to_rpm[buildreq]
                print "%s: %s" % (os.path.join( rpm_dir, rpmname ), 
                                  os.path.join( rpm_dir, buildreqrpm ) )


# Generate targets to build all srpms and all rpms
all_srpms = [ os.path.join( srpm_dir, srpmNameFromSpec( s ) ) 
              for s in specs.values() ]

all_rpms = []
for spec in specs.values():
    rpms = rpmNamesFromSpec( spec )
    rpm_paths = map( (lambda rpm: os.path.join( rpm_dir, rpm )), rpms )
    all_rpms += rpm_paths
    print "%s: %s" % ( spec.sourceHeader['name'], " ".join( rpm_paths ) )


print "rpms: " + " \\\n\t".join( all_rpms )
print "srpms: " + " \\\n\t".join( all_srpms )


print "install: all" 
print "\t. scripts/%s/install.sh" % buildType()
