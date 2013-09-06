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
from tree import Tree


def rulesFromSpec(spec, specpath):
    # XXX make each helper return a subtree and merge them at this level?
    # XXX write some tests!
    res = Tree()
    ocamlRulesPreamble(spec, res)
    rulesConfigureFromSpec(spec, res)
    rulesBuildFromSpec(spec, res)
    rulesInstallFromSpec(spec, res)
    rulesDhInstallFromSpec(spec, res, specpath)   # XXX need to augment the specfile object
    rulesCleanFromSpec(spec, res)
    rulesTestFromSpec(spec, res)
    return res

# XXX move all this into a separate file

def ocamlRulesPreamble(spec, tree):
    # should only include this at the end, if we noticed that we have packed up ocaml files
    # similarly for python files
    rule  = "#!/usr/bin/make -f\n"
    rule += "\n"
    rule += "#include /usr/share/cdbs/1/rules/debhelper.mk\n"
    rule += "#include /usr/share/cdbs/1/class/makefile.mk\n"
    rule += "#include /usr/share/cdbs/1/rules/ocaml.mk\n"
    rule += "\n"
    rule += "export DH_VERBOSE=1\n"
    rule += "export DH_OPTIONS\n"
    rule += "export DESTDIR=$(CURDIR)/debian/tmp\n"
    rule += "%:\n"
    rule += "\tdh $@ --with ocaml\n"
    rule += "\n"

    tree.append('debian/rules', rule)


def rulesConfigureFromSpec(spec, tree):
    # RPM doesn't have a configure target - everything happens in the
    # build target.  Nevertheless we must override the auto_configure target
    # because some OASIS packages have configure scripts.    If debhelper
    # sees a configure script it will assume it's from autoconf and will
    # run it with arguments that an OASIS configure script won't understand.

    rule = ".PHONY: override_dh_auto_configure\n"
    rule += "override_dh_auto_configure:\n"
    rule += "\n"

    tree.append('debian/rules', rule)


def rulesBuildFromSpec(spec, tree):
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

    if not spec.build:
        return {}

    rule =  ".PHONY: override_dh_auto_build\n"
    rule += "override_dh_auto_build:\n"
    rule += "\tdebian/build.sh\n"
    rule += "\n"

    helper = "#!/bin/sh\n"
    helper += "unset CFLAGS\n" #XXX HACK for ocaml-oclock
    helper += spec.build.replace("$RPM_BUILD_ROOT", "${DESTDIR}")

    tree.append('debian/rules', rule)
    tree.append('debian/build.sh', helper, permissions=0o755)


def rulesInstallFromSpec(spec, tree):
    rule =  ".PHONY: override_dh_auto_install\n"
    rule += "override_dh_auto_install:\n"
    rule += "\tdebian/install.sh\n"
    rule += "\n"

    helper = "#!/bin/sh\n" 
    helper += spec.install.replace("$RPM_BUILD_ROOT", "${DESTDIR}")

    tree.append('debian/rules', rule)
    tree.append('debian/install.sh', helper, permissions=0o755)

def rulesDhInstallFromSpec(spec, tree, specpath):
    rule  =  ".PHONY: override_dh_install\n"
    rule += "override_dh_install:\n"
    rule += "\tdh_install\n"

    pkgname = mappkgname.mapPackageName(spec.sourceHeader)
    files = rpmextra.filesFromSpec(pkgname, specpath)
    if files.has_key( pkgname + "-%exclude" ):
        for pat in files[pkgname + "-%exclude"]:
            path = "\trm -f debian/%s/%s\n" % (pkgname, rpm.expandMacro(pat))
 	    rule += os.path.normpath(path)
    rule += "\n"

    tree.append('debian/rules', rule)



def rulesCleanFromSpec(spec, tree):
    rule = ".PHONY: override_dh_auto_clean\n"
    rule += "override_dh_auto_clean:\n"
    rule += "\tdebian/clean.sh\n"
    rule += re.sub("^", "\t", spec.clean.strip(), flags=re.MULTILINE)
    rule += "\n\n"

    helper = "#!/bin/sh\n" + spec.clean.replace("$RPM_BUILD_ROOT", "${DESTDIR}")

    tree.append('debian/rules', rule)
    tree.append('debian/clean.sh', helper, permissions=0o755)


def rulesTestFromSpec(spec, tree):
    # XXX HACK for ocaml-oclock - don't try to run the tests when building
    rule  = ".PHONY: override_dh_auto_test\n"
    rule += "override_dh_auto_test:\n"

    tree.append('debian/rules', rule)

