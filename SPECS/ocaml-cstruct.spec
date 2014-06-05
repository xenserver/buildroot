%global debug_package %{nil}

Name:           ocaml-cstruct
Version:        0.7.1
Release:        3%{?dist}
Summary:        Read and write low-level C-style structures in OCaml
License:        ISC
URL:            https://github.com/mirage/ocaml-cstruct
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocplib-endian-devel

%description
Read and write low-level C-style structures in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-ocplib-endian-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --enable-lwt
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install DESTDIR=%{buildroot}

%files
%doc README.md
%doc CHANGES
%{_libdir}/ocaml/cstruct
%exclude %{_libdir}/ocaml/cstruct/*.a
%exclude %{_libdir}/ocaml/cstruct/*.cmxa
%exclude %{_libdir}/ocaml/cstruct/*.cmx
%exclude %{_libdir}/ocaml/cstruct/*.mli
%{_libdir}/ocaml/stublibs/dllcstruct_stubs.so
%{_libdir}/ocaml/stublibs/dllcstruct_stubs.so.owner

%files devel
%{_libdir}/ocaml/cstruct/*.a
%{_libdir}/ocaml/cstruct/*.cmx
%{_libdir}/ocaml/cstruct/*.cmxa
%{_libdir}/ocaml/cstruct/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.7.1-3
- Split files correctly between base and devel packages

* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.7.1-2
- Add dependency on lwt so the cstruct.lwt package is built

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

