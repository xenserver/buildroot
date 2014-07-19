%define debug_package %{nil}

Name:           ocaml-mirage-clock-xen
Version:        1.0.0
Release:        1%{?dist}
Summary:        A Mirage-compatible Clock library for Xen
License:        ISC
URL:            https://github.com/mirage/mirage-clock/
Source0:        https://github.com/mirage/mirage-clock/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mirage-types-devel

%description
A Mirage-compatible Clock library for Xen

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-clock-%{version}

%build
make xen-build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
make xen-install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/mirage-clock-xen
%exclude %{_libdir}/ocaml/mirage-clock-xen/*.a
%exclude %{_libdir}/ocaml/mirage-clock-xen/*.cmxa
%exclude %{_libdir}/ocaml/mirage-clock-xen/*.cmx

%files devel
%{_libdir}/ocaml/mirage-clock-xen/*.a
%{_libdir}/ocaml/mirage-clock-xen/*.cmx
%{_libdir}/ocaml/mirage-clock-xen/*.cmxa

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
