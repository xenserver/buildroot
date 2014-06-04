%define debug_package %{nil}

Name:           ocaml-shared-memory-ring
Version:        1.0.0
Release:        1%{?dist}
Summary:        OCaml implementation of Xen memory protocols
License:        ISC
URL:            https://github.com/mirage/shared-memory-ring/
Source0:        https://github.com/mirage/shared-memory-ring/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel

%description
This is a pure OCaml implementation of Xen-style shared memory rings.
These can be used for RPCs (disk requests, network packets) and for streaming
(xenstore, consoles)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-io-page-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n shared-memory-ring-%{version}

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
%{_libdir}/ocaml/shared-memory-ring
%exclude %{_libdir}/ocaml/shared-memory-ring/*.a
%exclude %{_libdir}/ocaml/shared-memory-ring/*.cmxa
%exclude %{_libdir}/ocaml/shared-memory-ring/*.cmx
%exclude %{_libdir}/ocaml/shared-memory-ring/*.mli

%files devel
%{_libdir}/ocaml/shared-memory-ring/*.a
%{_libdir}/ocaml/shared-memory-ring/*.cmx
%{_libdir}/ocaml/shared-memory-ring/*.cmxa
%{_libdir}/ocaml/shared-memory-ring/*.mli

%changelog
* Wed Jun 04 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
