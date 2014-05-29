%define debug_package %{nil}

Name:           ocaml-mirage-types
Version:        1.1.1
Release:        1%{?dist}
Summary:        MirageOS interfaces
License:        ISC
URL:            https://github.com/mirage/mirage
Source0:        http://github.com/mirage/mirage/archive/%{version}/mirage-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-ipaddr-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel

%description
This library contains interfaces to build applications that are compatible with the Mirage operating system. It defines only interfaces, and no concrete modules.

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
make build-types

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
#export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install-types

%clean
rm -rf %{buildroot}

%files
%{_libdir}/ocaml/mirage-types
%exclude %{_libdir}/ocaml/mirage-types/*.mli

%files devel
%{_libdir}/ocaml/mirage-types/*.mli


%changelog
* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-1
- Initial package
