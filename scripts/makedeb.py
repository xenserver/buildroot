#!/usr/bin/python

import glob
import mappkgname
import os
import re
import rpm
import rpmextra
import shutil
import subprocess
import sys

import debianchangelog
import debiancontrol
import debianmisc
import debianrules

# BUGS:
#   Hack to disable CFLAGS for ocaml-oclock
#   Hack to disable tests for ocaml-oclock
#   Hard coded install files only install ocaml dir
#   Should be building signed debs


# By default, RPM expects everything to be in $HOME/rpmbuild.  
# We want it to run in the current directory.
rpm.addMacro('_topdir', os.getcwd())


# Directories where rpmbuild expects to find inputs
# and writes outputs
SRPM_DIR = rpm.expandMacro('%_srcrpmdir')
SRC_DIR = rpm.expandMacro('%_sourcedir')
BUILD_DIR = rpm.expandMacro('%_builddir')


# Fedora puts executables run by other programs in /usr/libexec, but 
# Debian puts them in /usr/lib, which apparently follows the FHS:
# http://www.debian.org/doc/manuals/maint-guide/advanced.en.html#ftn.idp2018768
rpm.addMacro('_libexecdir', "/usr/lib")


# Override some macros interpolated into build rules, so
# paths are appropriate for debuild
# (Actually, using {}, not (), because these identifiers
# end up in helper scripts, not in the makefile
rpm.addMacro("buildroot", "${DESTDIR}")
rpm.addMacro("_libdir", "/usr/lib")


def debian_dir_from_spec(spec, path, specpath, isnative):
    os.makedirs(os.path.join(path, "debian/source"))

    control = debiancontrol.control_from_spec(spec)
    control.apply(path)

    rules = debianrules.rules_from_spec(spec, specpath)
    rules.apply(path)

    compat = debianmisc.compat_from_spec(spec)
    compat.apply(path)

    fmt = debianmisc.format_from_spec(spec, isnative)
    fmt.apply(path)

    copyright_file = debianmisc.copyright_from_spec(spec)
    copyright_file.apply(path)

    changelog = debianchangelog.changelog_from_spec(spec)
    changelog.apply(path)

    filelists = debianmisc.filelists_from_spec(spec, specpath)
    filelists.apply(path)

    patches = debianmisc.patches_from_spec(spec, SRC_DIR)
    patches.apply(path)

    conffiles = debianmisc.conffiles_from_spec(spec, specpath)
    conffiles.apply(path)


def principal_source_file(spec):
    return os.path.basename([name for (name, seq, filetype) 
                             in spec.sources 
                             if seq == 0 and filetype == 1][0])


def prepare_build_dir(spec, build_subdir):
    # To prepare the build dir, RPM cds into $TOPDIR/BUILD
    # and expands all paths in the prep script with $TOPDIR.
    # It unpacks the tarball and then cds into the directory it
    # creates before applying patches.
    # $TOPDIR should be an absolute path to the top RPM build
    # directory, not a relative path, so that references to SOURCES
    # expand to reachable paths inside the source tree (getting the 
    # tarball from ../SOURCES works in the outer BUILD dir, but getting
    # patches from ../SOURCES doesn't work when we have cd'ed into the
    # source tree.

    unpack_dir = os.path.join(BUILD_DIR, build_subdir)
    subprocess.call(spec.prep.replace("$RPM_BUILD_ROOT", unpack_dir), 
                    shell=True)
    # could also just do: RPMBUILD_PREP = 1<<0; spec._doBuild()

    
def rename_source(spec, pkgname, pkgversion):
    # Debian source package name should probably match the tarball name
    origfilename = principal_source_file(spec)
    if origfilename.endswith(".tbz"):
        filename = origfilename[:-len(".tbz")] + ".tar.bz2"
    else:
        filename = origfilename
    match = re.match("^(.+)(\.tar\.(gz|bz2|lzma|xz))", filename)
    if not match:
        print "error: could not parse filename %s" % filename
    _, ext = match.groups()[:2]
    base_filename = "%s_%s.orig%s" % (mappkgname.map_package(pkgname)[0], 
                                      pkgversion, ext)
    shutil.copy(os.path.join(SRC_DIR, origfilename), 
                os.path.join(BUILD_DIR, base_filename))


def main():
    shutil.rmtree(BUILD_DIR)
    os.mkdir(BUILD_DIR)
    spec = rpmextra.spec_from_file(sys.argv[1])
    clean = True
    if "-noclean" in sys.argv:
        clean = False

    # subdirectory of builddir in which the tarball is unpacked;  
    # set by RPM after processing the spec file
    # if the source file isn't a tarball this won't be set!
    build_subdir = rpm.expandMacro("%buildsubdir")  
    prepare_build_dir(spec, build_subdir)

    if os.path.isdir(os.path.join(BUILD_DIR, build_subdir, "debian")):
        shutil.rmtree(os.path.join(BUILD_DIR, build_subdir, "debian"))

    # a package with no original tarball is built as a 'native debian package'
    native = True
    tarball = principal_source_file(spec)
    match = re.match("^(.+)((\.tar\.(gz|bz2|lzma|xz)|\.tbz)$)", tarball)
    if match:
        native = False
         
        # copy over the source, run the prep rule to unpack it, then
        # rename it as deb expects this should be based on the rewritten
        # (or not) source name in the debian package - build the debian
        # dir first and then rename the tarball as needed
        rename_source(spec, spec.sourceHeader['name'], 
                      spec.sourceHeader['version']) 

    debian_dir_from_spec(spec, os.path.join(BUILD_DIR, build_subdir), 
                         sys.argv[1], native)

    res = subprocess.call("cd %s\ndpkg-source -b --auto-commit %s" % 
                          (BUILD_DIR, build_subdir), shell=True)
    assert res == 0

    if clean:
        shutil.rmtree(os.path.join(BUILD_DIR, build_subdir))
    for i in glob.glob(os.path.join(BUILD_DIR, "*")):
        if build_subdir in i:
            continue
        shutil.copy2(i, SRPM_DIR)
        if clean:
            os.unlink(i)

    # At this point we have a debian source package (at least 3 files) in SRPMS.
    # To build:
    #    pbuilder --create --distribution raring --architecture amd64 \
    #       --debootstrap qemu-debootstrap --mirror http://ports.ubuntu.com \
    #       --basetgz /var/cache/pbuilder/qemu-raring-armhf-base.tar.gz
    #
    # To build for ARM:
    #    pbuilder --create --distribution raring --architecture armhf \
    #       --debootstrap qemu-debootstrap --mirror http://ports.ubuntu.com \
    #       --basetgz /var/cache/pbuilder/qemu-raring-armhf-base.tar.gz


if __name__ == '__main__':
    main()

