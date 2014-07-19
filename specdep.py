#!/usr/bin/python

# see http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch16s04.html

import argparse
import os
import pkg
import platform
import sys
import urlparse

from scripts.lib import mappkgname


def build_type():
    debian_like = ["ubuntu", "debian", "linaro"]
    rhel_like = ["fedora", "redhat", "centos"]

    dist = platform.linux_distribution(full_distribution_name=False)[0].lower()
    assert dist in debian_like + rhel_like

    if dist in debian_like:
        return "deb"
    elif dist in rhel_like:
        return "rpm"


# Rules to build SRPM from SPEC
def build_srpm_from_spec(spec):
    srpmpath = spec.source_package_path()
    print '%s: %s %s' % (srpmpath, spec.specpath(),
                         " ".join(spec.source_paths()))



# Rules to download sources

# Assumes each RPM only needs one download - we have some multi-source
# packages but in all cases the additional sources are patches provided
# in the Git repository
def download_rpm_sources(spec):
    for (url, path) in zip(spec.source_urls(), spec.source_paths()):
        source = urlparse.urlparse(url)

        # Source comes from a remote HTTP server
        if source.scheme in ["http", "https"]:
            print '%s: %s' % (path, spec.specpath())
            print '\t@echo [DOWNLOADER] $@'
            print '\t@./scripts/downloader.py %s %s' % (url, path)

        # Source comes from a local file or directory
        if source.scheme == "file":
            print '%s: %s $(shell find %s)' % (
                path, spec.specpath(), source.path)

            # Assume that the directory name is already what's expected by the
            # spec file, and prefix it with the version number in the tarball
            print '\t@echo [GIT] $@'
            dirname = "%s-%s" % (os.path.basename(source.path), spec.version())
            print '\t@git --git-dir=%s/.git '\
                'archive --prefix %s/ -o $@ HEAD' % (source.path, dirname)


# Rules to build RPMS from SRPMS (uses information from the SPECs to
# get packages)
def build_rpm_from_srpm(spec):
    # We only generate a rule for the first binary RPM produced by the
    # specfile.  If we generate multiple rules (one for the base package,
    # one for -devel and so on), make will interpret these as completely
    # separate targets which must be built separately.   At best, this means
    # that the same package will be built more than once; at worst, in a 
    # concurrent build, there is a risk that the targets might not be rebuilt 
    # correctly.
    #
    # Make does understand the concept of multiple targets being built by
    # a single rule invocation, but only for pattern rules (e.g. %.h %.c: %.y).
    # It is tricky to generate correct pattern rules for RPM builds.

    rpm_path = spec.binary_package_paths()[0]
    srpm_path = spec.source_package_path()
    print '%s: %s' % (rpm_path, srpm_path)


def package_to_rpm_map(specs):
    provides_to_rpm = {}
    for spec in specs:
        for provided in spec.provides():
            provides_to_rpm[provided] = spec.binary_package_paths()[0]
    return provides_to_rpm


def buildrequires_for_rpm(spec, provides_to_rpm):
    rpmpath = spec.binary_package_paths()[0]
    for buildreq in spec.buildrequires():
        # Some buildrequires come from the system repository
        if provides_to_rpm.has_key(buildreq):
            buildreqrpm = provides_to_rpm[buildreq]
            print "%s: %s" % (rpmpath, buildreqrpm)


def parse_cmdline():
    """
    Parse command line options
    """
    parser = argparse.ArgumentParser(description=
        "Generate Makefile dependencies from RPM Spec files")
    parser.add_argument("specs", metavar="SPEC", nargs="+", help="spec file")
    parser.add_argument("-i", "--ignore", metavar="PKG", action="append",
        default=[], help="package name to ignore")
    parser.add_argument("-I", "--ignore-from", metavar="FILE", action="append",
        default=[], help="file of package names to be ignored")
    parser.add_argument("-d", "--dist", metavar="DIST",
        default="", help="distribution tag (used in RPM filenames)")
    return parser.parse_args()


def main():
    args = parse_cmdline()
    specs = {}
   
    pkgs_to_ignore = args.ignore
    for ignore_from in args.ignore_from:
        with open(ignore_from) as f:
            for name in f.readlines():
                pkgs_to_ignore.append(name.strip())
    for i in pkgs_to_ignore:
      print "# Will ignore: %s" % i

    for spec_path in args.specs:
        try:
            if build_type() == "deb":
                os_type = platform.linux_distribution(full_distribution_name=False)[1].lower()
                map_name_fn=lambda name: mappkgname.map_package(name, os_type)
                spec = pkg.Spec(spec_path, target="deb", map_name=map_name_fn)
            else:
                spec = pkg.Spec(spec_path, target="rpm", dist=args.dist)
            pkg_name = spec.name()
            if pkg_name in pkgs_to_ignore:
                continue

            specs[os.path.basename(spec_path)] = spec

        except pkg.SpecNameMismatch as exn:
            sys.stderr.write("error: %s\n" % exn.message)
            sys.exit(1)

    provides_to_rpm = package_to_rpm_map(specs.values())

    for spec in specs.itervalues():
        build_srpm_from_spec(spec)
        download_rpm_sources(spec)
        build_rpm_from_srpm(spec)
        buildrequires_for_rpm(spec, provides_to_rpm)
        print ""

    # Generate targets to build all srpms and all rpms
    all_rpms = []
    all_srpms = []
    for spec in specs.itervalues():
        rpm_path = spec.binary_package_paths()[0]
        all_rpms.append(rpm_path)
        all_srpms.append(spec.source_package_path())
        print "%s: %s" % (spec.name(), rpm_path)
    print ""

    print "rpms: " + " \\\n\t".join(all_rpms)
    print ""
    print "srpms: " + " \\\n\t".join(all_srpms)
    print ""
    print "install: all"
    print "\t. scripts/%s/install.sh" % build_type()


if __name__ == "__main__":
    main()
