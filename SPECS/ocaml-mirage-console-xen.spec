%define debug_package %{nil}

Name:           ocaml-mirage-console-xen
Version:        1.0.2
Release:        1%{?dist}
Summary:        A Mirage-compatible Console library for Xen
License:        ISC
URL:            https://github.com/mirage/mirage-console/
Source0:        https://github.com/mirage/mirage-console/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-mirage-xen-devel
BuildRequires:  ocaml-evtchn-devel
BuildRequires:  ocaml-gnt-devel

%description
A Mirage-compatible Console library for Xen

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-console-%{version}

%build
make xen-build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=ignore
make xen-install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/mirage-console-xen
%exclude %{_libdir}/ocaml/mirage-console-xen/*.a
%exclude %{_libdir}/ocaml/mirage-console-xen/*.cmxa
%exclude %{_libdir}/ocaml/mirage-console-xen/*.cmx

%files devel
%{_libdir}/ocaml/mirage-console-xen/*.a
%{_libdir}/ocaml/mirage-console-xen/*.cmx
%{_libdir}/ocaml/mirage-console-xen/*.cmxa

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.0.2-1
- Initial package
