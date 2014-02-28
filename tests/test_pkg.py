# Run these tests with 'nosetests':
#   install the 'python-nose' package (Fedora/CentOS or Ubuntu)
#   run 'nosetests' in the root of the repository

import unittest

import pkg

class RpmTests(unittest.TestCase):
    def setUp(self):
        self.spec = pkg.Spec("tests/SPECS/ocaml-cohttp.spec", dist=".el6")

    def test_good_filename_preprocessor(self):
        pkg.Spec("tests/SPECS/ocaml-cohttp.spec.in")

    def test_bad_filename(self):
        self.assertRaises(pkg.SpecNameMismatch, pkg.Spec, "tests/SPECS/bad-name.spec")

    def test_bad_filename_preprocessor(self):
        self.assertRaises(pkg.SpecNameMismatch, pkg.Spec, "tests/SPECS/bad-name.spec.in")

    def test_name(self):
        assert self.spec.name() == "ocaml-cohttp"

    def test_specpath(self):
        assert self.spec.specpath() == "./SPECS/ocaml-cohttp.spec"

    def test_version(self):
        assert self.spec.version() == "0.9.8"

    def test_provides(self):
        assert self.spec.provides() == \
            set(["ocaml-cohttp", "ocaml-cohttp-devel"])

    def test_source_urls(self):
        assert sorted(self.spec.source_urls()) == \
            sorted(["https://github.com/mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8/ocaml-cohttp-0.9.8.tar.gz"])

    def test_source_paths(self):
        assert sorted(self.spec.source_paths()) == \
            sorted(["./SOURCES/ocaml-cohttp-0.9.8.tar.gz"])

    def test_buildrequires(self):
        assert self.spec.buildrequires() == \
            set(["ocaml", "ocaml-findlib", "ocaml-re-devel",
                 "ocaml-uri-devel", "ocaml-cstruct-devel",
                 "ocaml-lwt-devel", "ocaml-ounit-devel",
                 "ocaml-ocamldoc", "ocaml-camlp4-devel",
                 "openssl", "openssl-devel"])

    def test_source_package_path(self):
        assert self.spec.source_package_path() == \
            "./SRPMS/ocaml-cohttp-0.9.8-1.el6.src.rpm"

    def test_binary_package_paths(self):
        assert sorted(self.spec.binary_package_paths()) == \
            sorted(["./RPMS/x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm",
             "./RPMS/x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm"])


class DebTests(unittest.TestCase):
    def setUp(self):
        def map_rpm_to_deb(name):
            mapping = {"ocaml-cohttp": ["libcohttp-ocaml"],
                       "ocaml-cohttp-devel": ["libcohttp-ocaml-dev"],
                       "ocaml": ["ocaml-nox", "ocaml-native-compilers"],
                       "ocaml-findlib": ["ocaml-findlib"],
                       "ocaml-re-devel": ["libre-ocaml-dev"],
                       "ocaml-uri-devel": ["liburi-ocaml-dev"],
                       "ocaml-cstruct-devel": ["libcstruct-ocaml-dev"],
                       "ocaml-lwt-devel": ["liblwt-ocaml-dev"],
                       "ocaml-ounit-devel": ["libounit-ocaml-dev"],
                       "ocaml-ocamldoc": ["ocaml-nox"],
                       "ocaml-camlp4-devel": ["camlp4", "camlp4-extra"],
                       "openssl": ["libssl1.0.0"],
                       "openssl-devel": ["libssl-dev"]}
            return mapping[name]

        self.spec = pkg.Spec("SPECS/ocaml-cohttp.spec", target="deb",
                             map_name=map_rpm_to_deb)

    def test_name(self):
        assert self.spec.name() == "ocaml-cohttp"

    def test_specpath(self):
        assert self.spec.specpath() == "./SPECS/ocaml-cohttp.spec"

    def test_version(self):
        assert self.spec.version() == "0.9.8"

    def test_provides(self):
        assert self.spec.provides() == \
            set(["libcohttp-ocaml", "libcohttp-ocaml-dev"])

    def test_source_urls(self):
        assert sorted(self.spec.source_urls()) == \
            sorted(["https://github.com/mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8/ocaml-cohttp-0.9.8.tar.gz"])

    def test_source_paths(self):
        assert sorted(self.spec.source_paths()) == \
            sorted(["./SOURCES/ocaml-cohttp-0.9.8.tar.gz"])

    def test_buildrequires(self):
        assert self.spec.buildrequires() == \
            set(["ocaml-nox", "ocaml-native-compilers",
                 "ocaml-findlib", "libre-ocaml-dev",
                 "liburi-ocaml-dev", "libcstruct-ocaml-dev",
                 "liblwt-ocaml-dev", "libounit-ocaml-dev",
                 "camlp4", "camlp4-extra", "libssl1.0.0",
                 "libssl-dev"])

    def test_source_package_path(self):
        assert self.spec.source_package_path() == \
            "./SRPMS/libcohttp-ocaml_0.9.8-1.dsc"

    def test_binary_package_paths(self):
        assert sorted(self.spec.binary_package_paths()) == \
            sorted(["./RPMS/libcohttp-ocaml_0.9.8-1_amd64.deb",
             "./RPMS/libcohttp-ocaml-dev_0.9.8-1_amd64.deb"])

