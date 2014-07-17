%global debug_package %{nil}

Name:           ocaml-uuidm
Version:        0.9.5
Release:        3%{?dist}
Summary:        Universally Unique IDentifiers (UUIDs) for OCaml
License:        BSD3
URL:            http://erratique.ch/software/uuidm
Source0:        https://github.com/dbuenzli/uuidm/archive/v%{version}/uuidm-%{version}.tar.gz
Patch0:         uuidm.oasis.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
Uuidm is an OCaml module implementing 128 bits universally unique
identifiers version 3, 5 (named based with MD5, SHA-1 hashing) and 4
(random based) according to RFC 4122.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uuidm-%{version}
%patch0 -p1

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install
rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/uuidtrip

%files
%doc CHANGES
%doc README
%{_libdir}/ocaml/uuidm
%exclude %{_libdir}/ocaml/uuidm/*.a
%exclude %{_libdir}/ocaml/uuidm/*.cmxa
%exclude %{_libdir}/ocaml/uuidm/*.cmx
%exclude %{_libdir}/ocaml/uuidm/*.mli

%files devel
%{_libdir}/ocaml/uuidm/*.a
%{_libdir}/ocaml/uuidm/*.cmx
%{_libdir}/ocaml/uuidm/*.cmxa
%{_libdir}/ocaml/uuidm/*.mli

%changelog
* Mon Jun 02 2014 Euan Harris <euan.harris@citrix.com> - 0.9.5-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.5-2
- Switch to GitHub mirror

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.5-1
- Initial package

