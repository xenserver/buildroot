import rpm
from tree import Tree
import mappkgname
import os
import rpmextra

def conffiles_from_spec(spec, specpath):
    # Configuration files, not to be overwritten on upgrade.
    # Files in /etc are automatically marked as config files,
    # so we only need to list files here if they are in a 
    # different place.
    res = Tree()
    pkgname = mappkgname.map_package_name(spec.sourceHeader)
    files = rpmextra.files_from_spec(pkgname, specpath)
    if files.has_key( pkgname + "-%config" ):
        for filename in files[pkgname + "-%config"]:
            res.append('debian/conffiles', "%s\n" % filename)
    return res


def filelists_from_spec(spec, specpath):
    res = Tree()
    for pkg in spec.packages:
        name = "%s.install.in" % mappkgname.map_package_name(pkg.header)
        res.append("debian/%s" % name, 
                   files_from_pkg(spec.sourceHeader['name'], pkg, specpath))
    return res


def files_from_pkg(basename, pkg, specpath):
    # should be able to build this from the files sections - can't find how
    # to get at them from the spec object
    res = ""
    files = rpmextra.files_from_spec(basename, specpath)
    for filename in files.get(pkg.header['name'], []):
        rpm.addMacro("_libdir", "usr/lib")
        rpm.addMacro("_bindir", "usr/bin")

        # deb just wants relative paths
        src = rpm.expandMacro(filename).lstrip("/")  
        rpm.delMacro("_bindir")
        rpm.delMacro("_libdir")
        rpm.addMacro("_libdir", "/usr/lib")
        rpm.addMacro("_bindir", "/usr/bin")
        dst = rpm.expandMacro(filename)

        # destination paths should be directories, not files.
        # if the file is foo and the path is /usr/bin/foo, the
        # package will end up install /usr/bin/foo/foo 
        if not dst.endswith("/"):
            dst = os.path.dirname(dst)
        rpm.delMacro("_bindir")
        rpm.delMacro("_libdir")
        res += "%s %s\n" % (src, dst)
    return res


# Patches can be added to debian/patches, with a series file
# We use dpkg-source -b --auto-commit <dir>

def patches_from_spec(spec, src_dir):
    res = Tree()
    patches = [(seq, name) for (name, seq, typ) in spec.sources 
               if typ == 2]
    patches = [name for (seq, name) in sorted(patches)]
    for patch in patches:
        with open(os.path.join(src_dir, patch)) as patchfile:
            contents = patchfile.read()
            permissions = os.fstat(patchfile.fileno()).st_mode
        res.append(os.path.join("debian/patches", patch),
                   contents, permissions)
        res.append("debian/patches/series", "%s\n" % patch)
    return res


def compat_from_spec(_spec):
    res = Tree()
    res.append("debian/compat", "8")
    return res

def format_from_spec(_spec, isnative):
    res = Tree()
    fmt = "native" if isnative else "quilt" 
    res.append("debian/source/format", "3.0 (%s)\n" % fmt)
    return res

def copyright_from_spec(_spec):
    res = Tree()
    res.append("debian/copyright", "FIXME")
    return res

