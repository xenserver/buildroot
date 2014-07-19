%define debug_package %{nil}

Name:           ocaml-mirage
Version:        1.2.0
Release:        1%{?dist}
Summary:        MirageOS interfaces
License:        ISC
URL:            https://github.com/mirage/mirage
Source0:        https://github.com/mirage/mirage/archive/v%{version}/mirage-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-ipaddr-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-cmdliner-devel

%description
A library and a command-line tool for building Mirage applications.
See http://openmirage.org for more information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  ocaml-ipaddr-devel%{?_isa}
BuildRequires:  ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-%{version}

%build
make PREFIX=%{buildroot}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p %{buildroot}/bin
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/mirage
%exclude %{_libdir}/ocaml/mirage/*.a
%exclude %{_libdir}/ocaml/mirage/*.cmxa
%exclude %{_libdir}/ocaml/mirage/*.cmx
%exclude %{_libdir}/ocaml/mirage/*.mli
/bin/mirage

%files devel
%{_libdir}/ocaml/mirage/*.a
%{_libdir}/ocaml/mirage/*.cmx
%{_libdir}/ocaml/mirage/*.cmxa
%{_libdir}/ocaml/mirage/*.mli

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.2.0-1
- Initial package

* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-1
- Initial package

