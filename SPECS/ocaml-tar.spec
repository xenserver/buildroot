Name:           ocaml-tar
Version:        0.2.1
Release:        2%{?dist}
Summary:        OCaml parser and printer for tar-format data
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/djs55/ocaml-tar
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz 
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-camlp4-devel

%description
This is a pure OCaml library for reading and writing tar-format data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%files
%doc README.md
%{_libdir}/ocaml/tar
%exclude %{_libdir}/ocaml/tar/*.a
%exclude %{_libdir}/ocaml/tar/*.cmxa
%exclude %{_libdir}/ocaml/tar/*.cmx
%exclude %{_libdir}/ocaml/tar/*.mli

%files devel
%{_libdir}/ocaml/tar/*.a
%{_libdir}/ocaml/tar/*.cmx
%{_libdir}/ocaml/tar/*.cmxa
%{_libdir}/ocaml/tar/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.2.1-2
- Split files correctly between base and devel packages

* Fri Nov 15 2013 David Scott <dave.scott@eu.citrix.com> - 0.2.1-1
- Initial package
