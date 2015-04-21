%define debug_package %{nil}

Name:           ocaml-shared-block-ring
Version:        1.1.1
Release:        1%{?dist}
Summary:        OCaml implementation of shared block rings
License:        ISC
URL:            https://github.com/mirage/shared-block-ring/
Source0:        https://github.com/mirage/shared-block-ring/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-block-unix-devel
BuildRequires:  ocaml-mirage-clock-unix-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-cmdliner-devel

%description
The shared memory ring protocols are used for: xenstore, console, disk and network devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n shared-block-ring-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/shared-block-ring
%exclude %{_libdir}/ocaml/shared-block-ring/*.a
%exclude %{_libdir}/ocaml/shared-block-ring/*.cmxa
%exclude %{_libdir}/ocaml/shared-block-ring/*.cmx
%exclude %{_libdir}/ocaml/shared-block-ring/*.mli

%files devel
%{_libdir}/ocaml/shared-block-ring/*.a
%{_libdir}/ocaml/shared-block-ring/*.cmx
%{_libdir}/ocaml/shared-block-ring/*.cmxa
%{_libdir}/ocaml/shared-block-ring/*.mli

%changelog
* Sun Apr 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.1.1-1
- Initial package

