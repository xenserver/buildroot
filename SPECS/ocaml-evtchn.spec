%define debug_package %{nil}

Name:           ocaml-evtchn
Version:        1.0.5
Release:        1%{?dist}
Summary:        OCaml bindings for userspace Xen event channel controls
License:        ISC
URL:            https://github.com/mirage/ocaml-evtchn/
Source0:        https://github.com/mirage/ocaml-evtchn/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  xen-devel

%description
These APIs allow programs running in userspace to signal other domains
on the same host.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-io-page-devel%{?_isa}
Requires:       xen-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

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
%{_libdir}/ocaml/xen-evtchn
%exclude %{_libdir}/ocaml/xen-evtchn/*.a
%exclude %{_libdir}/ocaml/xen-evtchn/*.cmxa
%exclude %{_libdir}/ocaml/xen-evtchn/*.cmx
%exclude %{_libdir}/ocaml/xen-evtchn/*.ml
%exclude %{_libdir}/ocaml/xen-evtchn/*.mli

%files devel
%{_libdir}/ocaml/xen-evtchn/*.a
%{_libdir}/ocaml/xen-evtchn/*.cmx
%{_libdir}/ocaml/xen-evtchn/*.cmxa
%{_libdir}/ocaml/xen-evtchn/*.mli

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.0.5-1
- Update to 1.0.5

* Fri May 23 2014 David Scott <dave.scott@citrix.com> - 1.0.1-1
- Initial package
