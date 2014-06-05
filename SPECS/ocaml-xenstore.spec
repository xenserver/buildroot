%global debug_package %{nil}

Name:           ocaml-xenstore
Version:        1.2.4
Release:        2%{?dist}
Summary:        Xenstore protocol implementation in OCaml
License:        LGPL
URL:            https://github.com/mirage/ocaml-xenstore
Source0:        https://github.com/mirage/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
Conflicts:      xen-ocaml

%description
An implementation of the xenstore protocol in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Conflicts:      xen-ocaml-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
ocaml setup.ml -configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES 
%doc LICENSE
%doc README 
%{_libdir}/ocaml/xenstore
%exclude %{_libdir}/ocaml/xenstore/*.a
%exclude %{_libdir}/ocaml/xenstore/*.cmxa
%exclude %{_libdir}/ocaml/xenstore/*.cmx
%exclude %{_libdir}/ocaml/xenstore/*.mli

%files devel
%{_libdir}/ocaml/xenstore/*.a
%{_libdir}/ocaml/xenstore/*.cmxa
%{_libdir}/ocaml/xenstore/*.cmx
%{_libdir}/ocaml/xenstore/*.mli

%changelog
* Mon Jun  2 2014 Euan Harris <euan.harris@citrix.com> - 1.2.4-2
- Split files correctly between base and devel packages

* Wed Sep 11 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.4-1
- Update to 1.2.4 (fixes critical watching bug)

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 1.2.3

* Tue Jul  2 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

