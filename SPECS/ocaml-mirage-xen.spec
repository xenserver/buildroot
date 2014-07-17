%define debug_package %{nil}

Name:           ocaml-mirage-xen
Version:        1.1.1
Release:        1%{?dist}
Summary:        Mirage OS library for Xen compilation
License:        ISC
URL:            https://github.com/mirage/mirage-platform/
Source0:        https://github.com/mirage/mirage-platform/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        ocaml-mirage-xen.install.sh
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-mirage-clock-xen
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-shared-memory-ring-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-evtchn-devel
BuildRequires:  ocaml-gnt-devel
BuildRequires:  ocaml-mirage-types-devel

%description
Mirage OS library for Xen compilation

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-io-page-devel%{?_isa}
Requires:       ocaml-mirage-clock-xen-devel%{?_isa}
Requires:       ocaml-shared-memory-ring-devel%{?_isa}
Requires:       xen-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-platform-%{version}
cp %{SOURCE1} ocaml-mirage-xen.install.sh

%build
make xen-build

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
sh ./ocaml-mirage-xen.install.sh %{buildroot}%{_libdir}/ocaml %{buildroot}
echo Files in _build:
find _build -name "*.a"
echo Files in buildroot:
find %{buildroot}

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/mirage-xen
%exclude %{_libdir}/ocaml/mirage-xen/*.a
%exclude %{_libdir}/ocaml/mirage-xen/*.cmxa
%exclude %{_libdir}/ocaml/mirage-xen/*.cmx
%exclude %{_libdir}/ocaml/mirage-xen/*.o
%exclude %{_libdir}/ocaml/mirage-xen/*.lds

%files devel
%{_libdir}/ocaml/mirage-xen/*.a
%{_libdir}/ocaml/mirage-xen/*.cmx
%{_libdir}/ocaml/mirage-xen/*.cmxa
%{_libdir}/ocaml/mirage-xen/libxencaml.a
%{_libdir}/ocaml/mirage-xen/libocaml.a
%{_libdir}/ocaml/mirage-xen/libdiet.a
%{_libdir}/ocaml/mirage-xen/libm.a
%{_libdir}/ocaml/mirage-xen/libxen.a
%{_libdir}/ocaml/mirage-xen/longjmp.o
%{_libdir}/ocaml/mirage-xen/x86_64.o
%{_libdir}/ocaml/mirage-xen/mirage-x86_64.lds

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.1.1-1
- Initial package
