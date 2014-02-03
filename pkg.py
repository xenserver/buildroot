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


def flatten(lst):
    """Flatten a list of lists"""
    return sum(lst, [])


def identity(name):
    """Identity mapping"""
    return name


def identity_list(name):
    """Identity mapping, injected into a list"""
    return [name]


def map_arch_deb(arch):
    """Map RPM package architecture to equivalent Deb architecture"""
    if arch == "x86_64":
        return "amd64"
    elif arch == "noarch":
        return "all"
    else:
        return arch


class Spec(object):
    """Represents an RPM spec file"""

    def __init__(self, path, target="rpm", map_name=None):
        if target == "rpm":
            self.rpmfilenamepat = rpm.expandMacro('%_build_name_fmt')
            self.srpmfilenamepat = rpm.expandMacro('%_build_name_fmt')
            self.map_arch = identity

            # '%dist' in the host (where we build the source package)
            # might not match '%dist' in the chroot (where we build
            # the binary package).   We must override it on the host,
            # otherwise the names of packages in the dependencies won't
            # match the files actually produced by mock.
            self.chroot_dist = ".el6"
            rpm.addMacro('dist', self.chroot_dist)

        else:
            self.rpmfilenamepat = "%{NAME}_%{VERSION}-%{RELEASE}_%{ARCH}.deb"
            self.srpmfilenamepat = "%{NAME}_%{VERSION}-%{RELEASE}.dsc"
            self.map_arch = map_arch_deb
            self.chroot_dist = ""
            rpm.addMacro('dist', self.chroot_dist)

        if map_name:
            self.map_package_name = map_name
        else:
            self.map_package_name = identity_list


        self.path = os.path.join(SPECDIR, os.path.basename(path))

        with open(path) as spec:
            self.spectext = spec.readlines()

        self.spec = rpm.ts().parseSpec(path)


    def specpath(self):
        """Return the path to the spec file"""
        return self.path


    def provides(self):
        """Return a list of package names provided by this spec"""
        provides = flatten([pkg.header['provides'] + [pkg.header['name']]
                          for pkg in self.spec.packages])
        return set(flatten([self.map_package_name(p) for p in provides]))


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
        return set(flatten([self.map_package_name(r) for r
                           in self.spec.sourceHeader['requires']]))


    def source_package_path(self):
        """Return the path of the source package which building this
           spec will produce"""
        hdr = self.spec.sourceHeader
        rpm.addMacro('NAME', self.map_package_name(hdr['name'])[0])
        rpm.addMacro('VERSION', hdr['version'])
        rpm.addMacro('RELEASE', hdr['release'])
        rpm.addMacro('ARCH', 'src')

        # There doesn't seem to be a macro for the name of the source
        # rpm, but the name appears to be the same as the rpm name format.
        # Unfortunately expanding that macro gives us a leading 'src' that we
        # don't want, so we strip that off

        srpmname = os.path.basename(rpm.expandMacro(self.srpmfilenamepat))

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
            rpm.addMacro('NAME', self.map_package_name(hdr['name'])[0])
            rpm.addMacro('VERSION', hdr['version'])
            rpm.addMacro('RELEASE', hdr['release'])
            rpm.addMacro('ARCH', self.map_arch(hdr['arch']))
            rpmname = rpm.expandMacro(self.rpmfilenamepat)
            rpm.delMacro('NAME')
            rpm.delMacro('VERSION')
            rpm.delMacro('RELEASE')
            rpm.delMacro('ARCH')
            return os.path.join(RPMDIR, rpmname)
        return [rpm_name_from_header(pkg.header) for pkg in self.spec.packages]
