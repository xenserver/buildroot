from cStringIO import StringIO
import glob
import os
import sys
import unittest

import makemake

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.spec = makemake.spec_from_file("SPECS/ocaml-cohttp.spec")
        self.spec = makemake.spec_from_file("SPECS/ocaml-cohttp.spec")

    def test_rpm_names_from_spec(self):
        assert makemake.rpm_names_from_spec(self.spec) == \
            ["x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm", 
             "x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm"]

    def test_buildrequires_from_spec(self):
        assert makemake.buildrequires_from_spec(self.spec) == \
            set(["ocaml", "ocaml-findlib", "ocaml-re-devel", "ocaml-uri-devel", "ocaml-cstruct-devel", "ocaml-lwt-devel", "ocaml-ounit-devel", "ocaml-ocamldoc", "ocaml-camlp4-devel", "openssl", "openssl-devel"])


    def test_build_srpm_from_spec(self):
        makemake.build_srpm_from_spec(self.spec, "ocaml-cohttp.spec")

        assert sys.stdout.getvalue() == \
"""./SRPMS/ocaml-cohttp-0.9.8-1.src.rpm: ./SPECS/ocaml-cohttp.spec ./SOURCES/ocaml-cohttp-0.9.8.tar.gz
	@echo [RPMBUILD] $@
	@rpmbuild --quiet --define "_topdir ." -bs $<
"""

    def test_download_rpm_sources(self):
        makemake.download_rpm_sources(self.spec, "ocaml-cohttp.spec")

        assert sys.stdout.getvalue() == \
"""./SOURCES/ocaml-cohttp-0.9.8.tar.gz: ./SPECS/ocaml-cohttp.spec
	@echo [CURL] $@
	@curl --silent --show-error -L -o $@ https://github.com/mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8/ocaml-cohttp-0.9.8.tar.gz
"""

    def test_build_rpm_from_srpm(self):
        makemake.build_rpm_from_srpm(self.spec)

        assert sys.stdout.getvalue() == \
"""./RPMS/x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm: ./SRPMS/ocaml-cohttp-0.9.8-1.src.rpm
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir="./RPMS/x86_64" $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS
./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm: ./SRPMS/ocaml-cohttp-0.9.8-1.src.rpm
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir="./RPMS/x86_64" $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS
"""


    def test_buildrequires_for_rpm(self):
        spec_paths = glob.glob(os.path.join("./SPECS", "*.spec"))
        specs = [makemake.spec_from_file(spec_path) for spec_path in spec_paths]

        makemake.buildrequires_for_rpm(self.spec, makemake.package_to_rpm_map(specs))
        assert sys.stdout.getvalue() == \
"""./RPMS/x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-uri-devel-1.3.8-1.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-cstruct-devel-0.7.1-2.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-ounit-devel-1.1.2-3.el6.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-re-devel-1.2.1-1.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-lwt-devel-2.4.3-1.el6.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-uri-devel-1.3.8-1.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-cstruct-devel-0.7.1-2.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-ounit-devel-1.1.2-3.el6.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-re-devel-1.2.1-1.x86_64.rpm
./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.x86_64.rpm: ./RPMS/x86_64/ocaml-lwt-devel-2.4.3-1.el6.x86_64.rpm
"""

