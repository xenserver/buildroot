%global debug_package %{nil}

Name:           ocaml-cdrom
Version:        0.9.1
Release:        3%{?dist}
Summary:        Query the state of CDROM devices
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/cdrom
Source0:        https://github.com/xapi-project/cdrom/archive/cdrom-%{version}/cdrom-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild

%description
Simple C bindings which allow the state of CDROM devices (and discs
inside) to be queried under Linux.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cdrom-cdrom-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%files
%doc ChangeLog 
%doc README.md
%{_libdir}/ocaml/cdrom
%exclude %{_libdir}/ocaml/cdrom/*.a
%exclude %{_libdir}/ocaml/cdrom/*.cmxa
%exclude %{_libdir}/ocaml/cdrom/*.cmx
%exclude %{_libdir}/ocaml/cdrom/*.mli
%{_libdir}/ocaml/stublibs/dllstubs_cdrom.so
%{_libdir}/ocaml/stublibs/dllstubs_cdrom.so.owner

%files devel
%{_libdir}/ocaml/cdrom/*.a
%{_libdir}/ocaml/cdrom/*.cmx
%{_libdir}/ocaml/cdrom/*.cmxa
%{_libdir}/ocaml/cdrom/*.mli

%changelog
* Fri Apr 17 2014 Euan Harris <euan.harris@citrix.com> - 0.9.1-3
- Split files correctly between base and devel packages

* Tue May 28 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

