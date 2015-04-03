%define debug_package %{nil}

Name:           ocaml-vchan
Version:        2.0.2
Release:        1%{?dist}
Summary:        OCaml implementation of the Xen Vchan protocol
License:        ISC
URL:            https://github.com/mirage/ocaml-vchan/
Source0:        https://github.com/mirage/ocaml-vchan/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-evtchn-devel
BuildRequires:  ocaml-gnt-devel
BuildRequires:  ocaml-ipaddr-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-ounit-devel

%description
The Xen Vchan protocol allows high-bandwidth private communication channels
between VMs over shared memory.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-io-page-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/vchan
%exclude %{_libdir}/ocaml/vchan/*.a
%exclude %{_libdir}/ocaml/vchan/*.cmxa
%exclude %{_libdir}/ocaml/vchan/*.cmx
%exclude %{_libdir}/ocaml/vchan/*.mli

%files devel
%{_libdir}/ocaml/vchan/*.a
%{_libdir}/ocaml/vchan/*.cmx
%{_libdir}/ocaml/vchan/*.cmxa
%{_libdir}/ocaml/vchan/*.mli

%changelog
* Fri Apr  3 2015 David Scott <dave.scott@citrix.com> - 2.0.2-1
- Update to 2.0.2

* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
