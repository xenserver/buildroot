#!/usr/bin/python

import rpm
import rpmextra
import os
import urlparse
import sys
import textwrap
import time
import re
import magic
import shutil
import subprocess
import shlex
import glob
import mappkgname
import debianrules
import debiancontrol
import debianchangelog
import debianmisc

# BUGS:
#   Code is a mess
#   Hack to disable CFLAGS for ocaml-oclock
#   Hack to disable tests for ocaml-oclock
#   Hard coded install files only install ocaml dir
#   Should be building signed debs


# By default, RPM expects everything to be in $HOME/rpmbuild.  
# We want it to run in the current directory.
rpm.addMacro( '_topdir', os.getcwd() )


# Directories where rpmbuild expects to find inputs
# and writes outputs
top_dir = rpm.expandMacro( '%_topdir' )
rpm_dir = rpm.expandMacro( '%_rpmdir' )
spec_dir = rpm.expandMacro( '%_specdir' )
srpm_dir = rpm.expandMacro( '%_srcrpmdir' )
src_dir = rpm.expandMacro( '%_sourcedir' )
build_dir = rpm.expandMacro( '%_builddir' )

# Fedora puts executables run by other programs in /usr/libexec, but 
# Debian puts them in /usr/lib, which apparently follows the FHS:
# http://www.debian.org/doc/manuals/maint-guide/advanced.en.html#ftn.idp2018768
rpm.addMacro( '_libexecdir', "/usr/lib" )

# Override some macros interpolated into build rules, so
# paths are appropriate for debuild
# (Actually, using {}, not (), because these identifiers
# end up in helper scripts, not in the makefile
rpm.addMacro( "buildroot", "${DESTDIR}" )
rpm.addMacro( "_libdir", "/usr/lib" )





def debianDirFromSpec(spec, path, specpath, isnative):
    os.makedirs( os.path.join(path, "debian/source") )

    control = debiancontrol.control_from_spec(spec)
    control.apply(path)

    rules = debianrules.rulesFromSpec(spec, specpath)
    rules.apply(path)

    with open( os.path.join(path, "debian/compat"), "w" ) as compat:
        compat.write("8\n")

    with open( os.path.join(path, "debian/source/format"), "w" ) as format:
        if isnative:
            format.write("3.0 (native)\n")
        else:
            format.write("3.0 (quilt)\n")

    with open( os.path.join(path, "debian/copyright"), "w" ) as copyright:
        copyright.write("FIXME")

    changelog = debianchangelog.changelog_from_spec(spec)
    changelog.apply(path)

    filelists = debianmisc.filelists_from_spec(spec, specpath)
    filelists.apply(path)

    patches = debianmisc.patches_from_spec(spec, src_dir)
    patches.apply(path)

    conffiles = debianmisc.conffiles_from_spec(spec, specpath)
    conffiles.apply(path)

def principalSourceFile(spec):
    return os.path.basename([name for (name, seq, type) in spec.sources 
                             if seq == 0 and type == 1][0])

def prepareBuildDir(spec, build_subdir):
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

    unpack_dir = os.path.join(build_dir, build_subdir)
    subprocess.call(spec.prep.replace("$RPM_BUILD_ROOT", unpack_dir), shell=True)
    # could also just do: RPMBUILD_PREP = 1<<0; spec._doBuild()

    
def renameSource(origfilename, pkgname, pkgversion):
    # Debian source package name should probably match the tarball name
    origfilename = principalSourceFile(spec)
    if origfilename.endswith(".tbz"):
        filename = origfilename[:-len(".tbz")] + ".tar.bz2"
    else:
        filename = origfilename
    m = re.match( "^(.+)(\.tar\.(gz|bz2|lzma|xz))", filename )
    if not m:
        print "error: could not parse filename %s" % filename
    basename, ext = m.groups()[:2]
    baseFileName = "%s_%s.orig%s" % (mappkgname.mapPackage(pkgname)[0], pkgversion, ext)
    shutil.copy(os.path.join(src_dir, origfilename), os.path.join(build_dir, baseFileName))


# Instead of writing to all these files, we could just accumulate
# everything in a dictionary of path -> (content, perms) and then
# write the files at the end.

if __name__ == '__main__':
    shutil.rmtree(build_dir)   #XXX
    os.mkdir(build_dir)
    spec = rpmextra.specFromFile(sys.argv[1])
    clean = True
    if "-noclean" in sys.argv:
        clean = False

    # subdirectory of builddir in which the tarball is unpacked;  
    # set by RPM after processing the spec file
    # if the source file isn't a tarball this won't be set!
    build_subdir = rpm.expandMacro("%buildsubdir")  
    prepareBuildDir(spec, build_subdir)

    if os.path.isdir( os.path.join(build_dir, build_subdir, "debian") ):
        shutil.rmtree(os.path.join(build_dir, build_subdir, "debian"))

    # a package with no original tarball is built as a 'native debian package'
    native = True
    tarball = principalSourceFile(spec)
    m = re.match( "^(.+)((\.tar\.(gz|bz2|lzma|xz)|\.tbz)$)", tarball )
    if m:
        native = False
         

        # copy over the source, run the prep rule to unpack it, then rename it as deb expects
        # this should be based on the rewritten (or not) source name in the debian package - build the debian dir first and then rename the tarball as needed
        renameSource(tarball, spec.sourceHeader['name'], spec.sourceHeader['version']) 

    debianDirFromSpec(spec, os.path.join(build_dir, build_subdir), sys.argv[1], native)

    # pdebuild gives us source debs as well as binaries
    res = subprocess.call( "cd %s\ndpkg-source -b --auto-commit %s" % (build_dir, build_subdir), shell=True )
    #pbuild can build a dsc - pbuilder --build <dsc> --configfile pbuilder/pbuildrerc-amd64 --resultdir ...
    #res = subprocess.call( "cd %s\npdebuild --configfile %s --buildresult %s" % (os.path.join(build_dir, build_subdir), os.path.join(top_dir, "pbuilder/pbuilderrc-amd64"), rpm_dir), shell=True )
    assert res == 0
    if clean:
        shutil.rmtree(os.path.join(build_dir, build_subdir))
    for i in glob.glob(os.path.join(build_dir, "*")):
        if build_subdir in i:
            continue
        shutil.copy2(i, srpm_dir) #XXX
        if clean:
            os.unlink(i)

    # at this point we have a debian source package (at least 3 files) in SRPMS
    # to build it:
    #    (first time: pbuilder --create)
    #    dpkg-source -x SRPMS/ocaml-react-0.9.4.dsc
    #    cd ocaml-react-0.9.4
    #    pdebuild --config pbuilder/pbuilder.cfg --buildresult DEBS  (can we set up groups to avoid the sudo password prompt?)
    #
    # to build for arm:
    #    pbuilder --create --distribution raring --architecture armhf --debootstrap qemu-debootstrap --mirror http://ports.ubuntu.com --basetgz /var/cache/pbuilder/qemu-raring-armhf-base.tar.gz
    #    pdebuild -- --distribution raring --architecture armhf --debootstrap qemu-debootstrap --mirror http://ports.ubuntu.com --basetgz /var/cache/pbuilder/qemu-raring-armhf-base.tar.gz


