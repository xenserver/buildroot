# Run these tests with 'nosetests':
#   install the 'python-nose' package (Fedora/CentOS or Ubuntu)
#   run 'nosetests' in the root of the repository

import glob
import os
import sys
import unittest

import specdep
import pkg

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.spec = pkg.Spec("SPECS/ocaml-cohttp.spec", dist=".el6")

    def test_build_srpm_from_spec(self):
        specdep.build_srpm_from_spec(self.spec)

        self.assertEqual(sys.stdout.getvalue(),
            "./SRPMS/ocaml-cohttp-0.9.8-1.el6.src.rpm: "
                "./SPECS/ocaml-cohttp.spec "
                "./SOURCES/ocaml-cohttp-0.9.8.tar.gz\n")

    def test_download_rpm_sources(self):
        specdep.download_rpm_sources(self.spec)

        self.assertEqual(sys.stdout.getvalue(),
            "./SOURCES/ocaml-cohttp-0.9.8.tar.gz: ./SPECS/ocaml-cohttp.spec\n"
            "	@echo [CURL] $@\n"
            "	@curl --silent --show-error -L -o $@ https://github.com/"
                "mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8/"
                "ocaml-cohttp-0.9.8.tar.gz\n")

    def test_build_rpm_from_srpm(self):
        specdep.build_rpm_from_srpm(self.spec)

        self.assertEqual(sys.stdout.getvalue(),
            "./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm: "
                "./SRPMS/ocaml-cohttp-0.9.8-1.el6.src.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm: "
                "./SRPMS/ocaml-cohttp-0.9.8-1.el6.src.rpm\n")


    def test_buildrequires_for_rpm(self):
        spec_paths = glob.glob(os.path.join("./SPECS", "*.spec"))
        specs = [pkg.Spec(spec_path, dist='.el6') for spec_path in spec_paths]

        specdep.buildrequires_for_rpm(self.spec,
            specdep.package_to_rpm_map(specs))

        self.assertEqual(sys.stdout.getvalue(),
            "./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-uri-devel-1.3.8-1.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-cstruct-devel-0.7.1-2.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-ounit-devel-1.1.2-3.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-re-devel-1.2.1-1.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-lwt-devel-2.4.3-1.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-uri-devel-1.3.8-1.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-cstruct-devel-0.7.1-2.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-ounit-devel-1.1.2-3.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-re-devel-1.2.1-1.el6.x86_64.rpm\n"
            "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm: "
                "./RPMS/x86_64/ocaml-lwt-devel-2.4.3-1.el6.x86_64.rpm\n")
