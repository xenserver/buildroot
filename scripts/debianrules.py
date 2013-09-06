#!/usr/bin/python

import rpm
import rpmextra
import os
import re
import mappkgname
from tree import Tree


def rules_from_spec(spec, specpath):
    res = Tree()
    ocaml_rules_preamble(spec, res)
    rules_configure_from_spec(spec, res)
    rules_build_from_spec(spec, res)
    rules_install_from_spec(spec, res)
    rules_dh_install_from_spec(spec, res, specpath)
    rules_clean_from_spec(spec, res)
    rules_test_from_spec(spec, res)
    return res


def ocaml_rules_preamble(_spec, tree):
    # TODO: should only include if we have packed up ocaml files
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


def rules_configure_from_spec(_spec, tree):
    # RPM doesn't have a configure target - everything happens in the
    # build target.  Nevertheless we must override the auto_configure target
    # because some OASIS packages have configure scripts.    If debhelper
    # sees a configure script it will assume it's from autoconf and will
    # run it with arguments that an OASIS configure script won't understand.

    rule = ".PHONY: override_dh_auto_configure\n"
    rule += "override_dh_auto_configure:\n"
    rule += "\n"

    tree.append('debian/rules', rule)


def rules_build_from_spec(spec, tree):
    # RPM's build rule is just a script which is run at the appropriate time.
    # debian/rules is a Makefile.   Makefile recipes aren't shell scripts - each
    # line is run independently, so exports don't survive from line to line and
    # multi-line constructions such as if statements don't work.
    # To work around this, we put these recipes in helper scripts in the debian/
    # directory.

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


def rules_install_from_spec(spec, tree):
    rule =  ".PHONY: override_dh_auto_install\n"
    rule += "override_dh_auto_install:\n"
    rule += "\tdebian/install.sh\n"
    rule += "\n"

    helper = "#!/bin/sh\n" 
    helper += spec.install.replace("$RPM_BUILD_ROOT", "${DESTDIR}")

    tree.append('debian/rules', rule)
    tree.append('debian/install.sh', helper, permissions=0o755)

def rules_dh_install_from_spec(spec, tree, specpath):
    rule  =  ".PHONY: override_dh_install\n"
    rule += "override_dh_install:\n"
    rule += "\tdh_install\n"

    pkgname = mappkgname.map_package_name(spec.sourceHeader)
    files = rpmextra.files_from_spec(pkgname, specpath)
    if files.has_key( pkgname + "-%exclude" ):
        for pat in files[pkgname + "-%exclude"]:
            path = "\trm -f debian/%s/%s\n" % (pkgname, rpm.expandMacro(pat))
            rule += os.path.normpath(path)
    rule += "\n"

    tree.append('debian/rules', rule)



def rules_clean_from_spec(spec, tree):
    rule = ".PHONY: override_dh_auto_clean\n"
    rule += "override_dh_auto_clean:\n"
    rule += "\tdebian/clean.sh\n"
    rule += re.sub("^", "\t", spec.clean.strip(), flags=re.MULTILINE)
    rule += "\n\n"

    helper = "#!/bin/sh\n" + spec.clean.replace("$RPM_BUILD_ROOT", "${DESTDIR}")

    tree.append('debian/rules', rule)
    tree.append('debian/clean.sh', helper, permissions=0o755)


def rules_test_from_spec(_spec, tree):
    # XXX HACK for ocaml-oclock - don't try to run the tests when building
    rule  = ".PHONY: override_dh_auto_test\n"
    rule += "override_dh_auto_test:\n"

    tree.append('debian/rules', rule)

