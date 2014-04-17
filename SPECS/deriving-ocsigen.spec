Name:           deriving-ocsigen
Version:        0.3c
Release:        2%{?dist}
Summary:        Extension to OCaml for deriving functions from type declarations
License:        MIT
URL:            http://ocsigen.org
Source0:        http://ocsigen.org/download/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib

%description
Extension to OCaml for deriving functions from type declarations

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc COPYING
%doc README
%{_libdir}/ocaml/deriving-ocsigen
%exclude %{_libdir}/ocaml/deriving-ocsigen/*.a
%exclude %{_libdir}/ocaml/deriving-ocsigen/*.cmxa
%exclude %{_libdir}/ocaml/deriving-ocsigen/*.cmx
%exclude %{_libdir}/ocaml/deriving-ocsigen/*.mli

%files devel
%{_libdir}/ocaml/deriving-ocsigen/*.a
%{_libdir}/ocaml/deriving-ocsigen/*.cmx
%{_libdir}/ocaml/deriving-ocsigen/*.cmxa
%{_libdir}/ocaml/deriving-ocsigen/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.3c-2
- Split files correctly between base and devel packages

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.3c-1
- Initial package

