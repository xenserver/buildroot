"""Classes for handling RPM spec files.   The classes defined here
   are mostly just wrappers around rpm.rpm, adding information which
   the rpm library does not currently provide."""


import os
import rpm

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


def flatten(lst):
    """Flatten a list of lists"""
    res = []
    for elt in lst:
        res += elt
    return res


class Spec(object):
    """Represents an RPM spec file"""

    def __init__(self, specfile):
        # for debugging, make all paths relative to PWD
        #rpm.addMacro('_topdir', '.')

        # We could avoid hardcoding this by running
        # "mock -r xenserver --chroot "rpm --eval '%dist'"
        self.chroot_dist = '.el6'
        rpm.addMacro('dist', self.chroot_dist)

        self.rpmfilenamepat = rpm.expandMacro('%_build_name_fmt')

        with open(specfile) as spec:
            self.spectext = spec.readlines()

        self.spec = rpm.ts().parseSpec(specfile)


    def provides(self):
        """Return a list of package names provided by this spec"""
        provides = [pkg.header['provides'] + [pkg.header['name']]
                    for pkg in self.packages()]
        return set(flatten(provides))


    def name(self):
        """Return the package name"""
        return self.spec.sourceHeader['name']


    def version(self):
        """Return the package version"""
        return self.spec.sourceHeader['version']


    def packages(self):
        """Return package objects for each package the spec defines"""
        return self.spec.packages


    def sources(self):
        """Return the sources"""
        return [source for (source, _, _) in self.spec.sources]


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
        return [rpm_name_from_header(pkg.header) for pkg in self.packages()]
