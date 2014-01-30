"""Classes for handling RPM spec files.   The classes defined here
   are mostly just wrappers around rpm.rpm, adding information which
   the rpm library does not currently provide."""


import os
import rpm
import urlparse

# Could have a decorator / context manager to set and unset all the RPM macros
# around methods such as 'provides'


# for debugging, make all paths relative to PWD
rpm.addMacro('_topdir', '.')

# Directories where rpmbuild/mock expects to find inputs
# and writes outputs
RPMDIR  = rpm.expandMacro('%_rpmdir')
SRPMDIR = rpm.expandMacro('%_srcrpmdir')
SPECDIR = rpm.expandMacro('%_specdir')
SRCDIR  = rpm.expandMacro('%_sourcedir')

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
rpm.addMacro('dist', CHROOT_DIST)


def flatten(lst):
    """Flatten a list of lists"""
    res = []
    for elt in lst:
        res += elt
    return res


class Spec(object):
    """Represents an RPM spec file"""

    def __init__(self, path):
        self.rpmfilenamepat = rpm.expandMacro('%_build_name_fmt')

        self.path = os.path.join(SPECDIR, os.path.basename(path))

        with open(path) as spec:
            self.spectext = spec.readlines()

        self.spec = rpm.ts().parseSpec(path)


    def specpath(self):
        """Return the path to the spec file"""
        return self.path


    def provides(self):
        """Return a list of package names provided by this spec"""
        provides = [pkg.header['provides'] + [pkg.header['name']]
                    for pkg in self.spec.packages]
        return set(flatten(provides))


    def name(self):
        """Return the package name"""
        return self.spec.sourceHeader['name']


    def version(self):
        """Return the package version"""
        return self.spec.sourceHeader['version']


    def source_urls(self):
        """Return the URLs from which the sources can be downloaded"""
        return [source for (source, _, _) in self.spec.sources]


    def source_paths(self):
        """Return the filesystem paths to source files"""
        sources = []
        for source in self.source_urls():
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

        return sources



    # RPM build dependencies.   The 'requires' key for the *source* RPM is
    # actually the 'buildrequires' key from the spec
    def buildrequires(self):
        """Return the set of packages needed to build this spec
           (BuildRequires)"""
        return set([r for r in self.spec.sourceHeader['requires']])


    def source_package_path(self):
        """Return the path of the source package which building this
           spec will produce"""
        hdr = self.spec.sourceHeader
        rpm.addMacro('NAME', hdr['name'])
        rpm.addMacro('VERSION', hdr['version'])
        rpm.addMacro('RELEASE', hdr['release'])
        rpm.addMacro('ARCH', 'src')

        # There doesn't seem to be a macro for the name of the source
        # rpm, but the name appears to be the same as the rpm name format.
        # Unfortunately expanding that macro gives us a leading 'src' that we
        # don't want, so we strip that off

        srpmname = os.path.basename(rpm.expandMacro(self.rpmfilenamepat))

        rpm.delMacro('NAME')
        rpm.delMacro('VERSION')
        rpm.delMacro('RELEASE')
        rpm.delMacro('ARCH')

        return os.path.join(SRPMDIR, srpmname)


    def binary_package_paths(self):
        """Return a list of binary packages built by this spec"""
        def rpm_name_from_header(hdr):
            """Return the name of the binary package file which
               will be built from hdr"""
            rpm.addMacro('NAME', hdr['name'])
            rpm.addMacro('VERSION', hdr['version'])
            rpm.addMacro('RELEASE', hdr['release'])
            rpm.addMacro('ARCH', hdr['arch'])
            rpm.addMacro('ARCH', hdr['arch'])
            rpmname = rpm.expandMacro(self.rpmfilenamepat)
            rpm.delMacro('NAME')
            rpm.delMacro('VERSION')
            rpm.delMacro('RELEASE')
            rpm.delMacro('ARCH')
            return os.path.join(RPMDIR, rpmname)
        return [rpm_name_from_header(pkg.header) for pkg in self.spec.packages]
