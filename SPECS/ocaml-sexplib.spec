%global debug_package %{nil}

Name:           ocaml-sexplib
Version:        109.20.00
Release:        1
Summary:        Convert values to and from s-expressions in OCaml

Group:          Development/Libraries
License:        LGPLv2+ with exceptions and BSD
URL:            https://ocaml.janestreet.com
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/sexplib-%{version}.tar.gz

BuildRequires:  ocaml >= 4.00.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-type-conv

%description
Convert values to and from s-expressions in OCaml.

%prep
%setup -q -n sexplib-%{version}

%build
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install


%files
%defattr(-,root,root,-)
%doc CHANGES.txt COPYRIGHT.txt INRIA-DISCLAIMER.txt INSTALL.txt LICENSE-Tywith.txt LICENSE.txt README.md THIRD-PARTY.txt
%{_libdir}/ocaml/sexplib

%changelog
* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com> - 109.20.00-1
- Initial package

