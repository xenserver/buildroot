#!/usr/bin/python

import rpm
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

# BUGS:
#   Code is a mess
#   Hack to disable CFLAGS for ocaml-oclock
#   Hack to disable tests for ocaml-oclock
#   Hard coded install files only install ocaml dir


# By default, RPM expects everything to be in $HOME/rpmbuild.  
rpm.addMacro( '_topdir', os.getcwd() )


# Directories where rpmbuild/mock expects to find inputs
# and writes outputs
top_dir = rpm.expandMacro( '%_topdir' )
rpm_dir = rpm.expandMacro( '%_rpmdir' )
spec_dir = rpm.expandMacro( '%_specdir' )
srpm_dir = rpm.expandMacro( '%_srcrpmdir' )
src_dir = rpm.expandMacro( '%_sourcedir' )
build_dir = rpm.expandMacro( '%_builddir' )


# Override some macros interpolated into build rules, so
# paths are appropriate for debuild
# (Actually, using {}, not (), because these identifiers
# end up in helper scripts, not in the makefile
rpm.addMacro( "buildroot", "${DESTDIR}" )
rpm.addMacro( "_libdir", "${STDLIBDIR}" )


def specFromFile(spec):
    return rpm.ts().parseSpec(spec)


STANDARDS_VERSION = "3.9.3"


# Patches can be added to debian/patches, with a series file
# Files copied into this directory have to be added using dpkg-source --commit
# (possibly just initialize quilt in that directory and add them as we copy them)
# We can just use dpkg-source -b --auto-commit <dir>


def mapPackageBaseName(name):
    """rewrite an rpm name to fit with debian standards"""
    # Debian puts the language name after the library name
    # whereas Fedora puts it before
    if name.startswith( "ocaml-" ):
        name = name[ len("ocaml-"): ] + "-ocaml"

    return name


def mapPackageName(hdr):
    """rewrite an rpm name to fit with debian standards"""
    name = hdr['name']
    # XXX UGLY

    # Debian adds a -dev suffix to development packages,
    # whereas Fedora uses -devel
    isDevel = False
    if name.endswith( "-devel" ):
        isDevel = True
        name = name[ :-len("-devel") ]

    name = mapPackageBaseName(name)

    # Debian prefixes library packag names with 'lib'
    if "Libraries" in hdr['group']:
        name = "lib" + name
    if isDevel:
        name += "-dev"

    return name


def mapPackage(rpm_name):
    """map an rpm to a corresponding deb, based on file contents"""
    # XXXXX
    if rpm_name == "ocaml":
        return "ocaml-nox"
    if rpm_name == "ocaml-findlib-devel":
        return "ocaml-findlib"
    if rpm_name == "ocaml-findlib":
        return "ocaml-findlib"
    if rpm_name == "ocaml-ocamldoc":
        return "ocaml-nox"
    if rpm_name == "ocaml-re-devel":
        return "re-ocaml-dev"
    print "unrecognized package: %s" % rpm_name
    assert False


def mapSection(rpm_name):
    return "ocaml" # XXXXX


def formatDescription(description):
    """need to format this - correct line length, initial one space indent,
    and blank lines must be replaced by dots"""

    paragraphs = "".join(description).split("\n\n")
    wrapped = [ "\n".join(textwrap.wrap( p, initial_indent=" ", 
                                            subsequent_indent=" ")) 
                for p in paragraphs ]
    return "\n .\n".join( wrapped )


def sourceDebFromSpec(spec):
    res = ""
    res += "Source: %s\n" % spec.sourceHeader['name'] #XXX should this be mapped?
    res += "Priority: %s\n" % "optional"
    res += "Maintainer: %s\n" % "Euan Harris <euan.harris@citrix.com>" #XXX
    res += "Section: %s\n" % mapSection(spec.sourceHeader['group'])
    res += "Standards-Version: %s\n" % STANDARDS_VERSION
    res += "Build-Depends:\n"
    build_depends = [ "debhelper (>= 8)", "dh-ocaml (>= 0.9)" ]
    for pkg, version in zip(spec.sourceHeader['requires'], spec.sourceHeader['requireVersion']):
        dep = mapPackage(pkg)
        if version:
            dep += " (>= %s)" % version
        build_depends.append(dep)
    res += ",\n".join( set([" %s" % d for d in build_depends]))
    res += "\n"
    return res


def binaryDebFromSpec(spec):
    res = ""
    res += "Package: %s\n" % mapPackageName(spec.header)
    res += "Architecture: any\n" # XXXX % spec.header['arch']
    res += "Depends:\n"
    depends = ["${ocaml:Depends}", "${shlibs:Depends}", "${misc:Depends}"]
    depends += [mapPackage(r) for r in spec.header['requires']]
    res += ",\n".join( [ " %s" % d for d in depends ] )
    res += "\n"
    res += "Provides: ${ocaml:Provides}\n"  # XXXX only for ocaml!
    res += "Recommends: ocaml-findlib\n" # XXXX 
    res += "Description: %s\n" % spec.header['summary']
    res += formatDescription( spec.header['description'] )
    res += "\n"
    return res


def debianControlFromSpec(spec):
    res = ""
    res += sourceDebFromSpec(spec)
    for pkg in spec.packages:
        res += "\n"
        res += binaryDebFromSpec(pkg)
    return res


def ocamlRulesPreamble():
    return """#!/usr/bin/make -f
#include /usr/share/cdbs/1/rules/debhelper.mk
#include /usr/share/cdbs/1/class/makefile.mk
#include /usr/share/cdbs/1/rules/ocaml.mk

export DH_VERBOSE=1
export DH_OPTIONS

export DESTDIR=$(CURDIR)/debian/tmp

%:
\tdh $@ --with ocaml

"""


def debianRulesFromSpec(spec, path):
    res = ""
    res += ocamlRulesPreamble()
    res += debianRulesConfigureFromSpec(spec)
    res += debianRulesBuildFromSpec(spec, path)
    res += debianRulesInstallFromSpec(spec, path)
    res += debianRulesCleanFromSpec(spec, path)
    res += debianRulesTestFromSpec(spec, path)
    return res

    
# RPM doesn't have a configure target - everything happens in the build target
def debianRulesConfigureFromSpec(spec):
#    return """.PHONY: override_dh_auto_configure
#override_dh_auto_configure:
#\tocaml setup.ml -configure --destdir $(DESTDIR)/$(OCAML_STDLIB_DIR)
#
#"""
    return ""


def debianRulesBuildFromSpec(spec, path):
    # RPM's build script is just a script which is run at the appropriate time.
    # debian/rules is a Makefile.   Makefile recipes aren't shell scripts - each
    # line is run independently, so exports don't survive from line to line and
    # multi-line constructions such as if statements don't work.
    # Tried wrapping everything in a $(shell ...) function, but that didn't work.
    # Just write the script fragment into a helper script in the debian directory.
    # This almost certainly violates a Debian packaging guideline...
    # ...we could write them to temporary files as the makefile is evaluated...
    # this sub-script business unfortunately means that variables from the makefile
    # aren't passed through
    # Hurray, the .ONESHELL special target may save us

    rule = ".PHONY: override_dh_auto_build\n"
    rule += "override_dh_auto_build:\n"
    rule += "\tdebian/build.sh\n"
    rule += "\n"
    with open(os.path.join(path, "debian/build.sh"), "w") as f:
        helper = "#!/bin/sh\n"
        helper += "unset CFLAGS\n" #XXX HACK for ocaml-oclock
        helper += spec.build
        f.write(helper)
    os.chmod(os.path.join(path, "debian/build.sh"), 0o755)
    return rule


def debianRulesInstallFromSpec(spec, path):
    rule = ".PHONY: override_dh_auto_install\n"
    rule += "override_dh_auto_install:\n"
    rule += "\tdebian/install.sh\n"
    rule += "\n"
    with open(os.path.join(path, "debian/install.sh"), "w") as f:
        f.write("#!/bin/sh\n" + spec.install)
    os.chmod(os.path.join(path, "debian/install.sh"), 0o755)
    return rule


def debianRulesTestFromSpec(spec, path):
    # XXX HACK for ocaml-oclock - don't try to run the tests when building
    rule = ".PHONY: override_dh_auto_test\n"
    rule += "override_dh_auto_test:\n"
    return rule


def debianRulesCleanFromSpec(spec, path):
    rule = ".PHONY: override_dh_auto_clean\n"
    rule += "override_dh_auto_clean:\n"
    rule += "\tdebian/clean.sh\n"
    rule += re.sub("^", "\t", spec.clean.strip(), flags=re.MULTILINE)
    rule += "\n"
    with open(os.path.join(path, "debian/clean.sh"), "w") as f:
        f.write("#!/bin/sh\n" + spec.clean)
    os.chmod(os.path.join(path, "debian/clean.sh"), 0o755)
    return rule


def debianChangelogFromSpec(spec):
    hdr = spec.sourceHeader
    res = ""
    for (name, timestamp, text) in zip(hdr['changelogname'], hdr['changelogtime'], hdr['changelogtext']):

        # Most spec files have "First Last <first@foo.com> - version"
        # Some of ours have "First Last <first@foo.com>" only for the first entry - could
        # be a mistake.  For these, us the version from the spec. 
        m = re.match( "^(.+) - (\S+)$", name )
        if m:
            author = m.group(1)
            version = m.group(2)
        else:
            author = name
            version = spec.sourceHeader['version']

        res += "%s (%s) UNRELEASED; urgency=low\n" % (hdr['name'], version)
        res += "\n"
	text = re.sub( "^-", "*", text, flags=re.MULTILINE )
	text = re.sub( "^", "  ", text, flags=re.MULTILINE )
        res += "%s\n" % text
        res += "\n"
        res += " -- %s  %s\n" % (author, time.strftime("%a, %d %b %Y %H:%M:%S %z", time.gmtime(int(timestamp))))
        res += "\n"
    return res


def debianFilesFromPkg(pkg):
    # should be able to build this from the files sections - can't find how
    # to get at them from the spec object
    res = ""
    res += "ocaml/*        @OCamlStdlibDir@/\n"   # should be more specific
    return res


def debianFilelistsFromSpec(spec, path):
    for pkg in spec.packages:
        name = "%s.install.in" % mapPackageName(pkg.header)
        with open( os.path.join(path, "debian/%s") % name, "w" ) as f:
            f.write( debianFilesFromPkg(pkg) )

def debianPatchesFromSpec(spec, path):
    patches = [(seq, name) for (name, seq, typ) in spec.sources 
               if typ == 2]
    patches = [name for (seq,name) in sorted(patches)]
    if patches:
        os.mkdir(os.path.join(path, "debian/patches"))
    for patch in patches:
        shutil.copy2(os.path.join(src_dir, patch), os.path.join(path, "debian/patches")) 
        with open( os.path.join(path, "debian/patches/series"), "a" ) as f:
            f.write("%s\n" % patch)



def debianDirFromSpec(spec, path):
    os.makedirs( os.path.join(path, "debian/source") )

    with open( os.path.join(path, "debian/control"), "w" ) as control:
        control.write(debianControlFromSpec(spec))

    with open( os.path.join(path, "debian/rules"), "w" ) as rules:
        rules.write(debianRulesFromSpec(spec, path))
    os.chmod( os.path.join(path, "debian/rules"), 0o755 )

    with open( os.path.join(path, "debian/compat"), "w" ) as compat:
        compat.write("8\n")

    with open( os.path.join(path, "debian/source/format"), "w" ) as format:
        format.write("3.0 (quilt)\n")

    with open( os.path.join(path, "debian/copyright"), "w" ) as copyright:
        copyright.write("FIXME")

    with open( os.path.join(path, "debian/changelog"), "w" ) as changelog:
        changelog.write(debianChangelogFromSpec(spec))

    debianFilelistsFromSpec(spec, path)
    debianPatchesFromSpec(spec, path)

def principalSourceFile(spec):
    return os.path.basename([name for (name, seq, type) in spec.sources 
                             if seq == 0 and type == 1][0])

def prepareBuildDir(spec):
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

    subprocess.call(spec.prep, shell=True)

    
def renameSource(spec):
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
    baseFileName = "%s_%s.orig%s" % (spec.sourceHeader['name'], spec.sourceHeader['version'], ext)
    shutil.copy(os.path.join(src_dir, origfilename), os.path.join(build_dir, baseFileName))

# Instead of writing to all these files, we could just accumulate
# everything in a dictionary of path -> (content, perms) and then
# write the files at the end.

if __name__ == '__main__':
    shutil.rmtree(build_dir)   #XXX
    os.mkdir(build_dir)
    spec = specFromFile(sys.argv[1])

    # subdirectory of builddir in which the tarball is unpacked;  
    # set by RPM after processing the spec file
    build_subdir = rpm.expandMacro("%buildsubdir")  
    prepareBuildDir(spec)

    tarball = principalSourceFile(spec)

    # copy over the source, run the prep rule to unpack it, then rename it as deb expects
    renameSource(spec) 
    
    debianDirFromSpec(spec, os.path.join(build_dir, build_subdir))
    
    # pdebuild gives us source debs as well as binaries
    #res = subprocess.call( "cd %s\ndpkg-source -b --auto-commit %s" % (build_dir, build_subdir), shell=True )
    res = subprocess.call( "cd %s\npdebuild --configfile %s --buildresult %s" % (os.path.join(build_dir, build_subdir), os.path.join(top_dir, "pbuilder/pbuilderrc-amd64"), rpm_dir), shell=True )
    assert res == 0
    shutil.rmtree(os.path.join(build_dir, build_subdir))
    for i in glob.glob(os.path.join(build_dir, "*")):
        shutil.copy2(i, srpm_dir) #XXX
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


