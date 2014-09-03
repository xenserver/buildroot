%global debug_package %{nil}

Name:           ocaml-xen-lowlevel-libs
Version:        0.9.25
Release:        2%{?dist}
Summary:        Xen hypercall bindings for OCaml
License:        LGPL
URL:            https://github.com/xapi-project/ocaml-xen-lowlevel-libs
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  libuuid-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  xen-devel
BuildRequires:  xen-missing-headers
BuildRequires:  ocaml-cstruct-devel

%description
Xen hypercall bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        runtime
Summary:        Runtime binaries for users of %{name}
Group:          Development/Libraries

%description    runtime
The %{name}-runtime package contains binaries which must be present
at runtime when executing programs that use %{name}.

%prep
%setup -q

%build
./configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install BINDIR=%{buildroot}/%{_libexecdir}/xenopsd/

%files
%doc README.md
%{_libexecdir}/xenopsd/xenguest
%{_libdir}/ocaml/xenctrl
%exclude %{_libdir}/ocaml/xenctrl/*.a
%exclude %{_libdir}/ocaml/xenctrl/*.cmxa
%exclude %{_libdir}/ocaml/xenctrl/*.cmx
%exclude %{_libdir}/ocaml/xenctrl/*.mli
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so.owner
%{_libdir}/ocaml/xenlight
%exclude %{_libdir}/ocaml/xenlight/*.a
%exclude %{_libdir}/ocaml/xenlight/*.cmxa
%exclude %{_libdir}/ocaml/xenlight/*.cmx
%exclude %{_libdir}/ocaml/xenlight/*.mli
%{_libdir}/ocaml/stublibs/dllxenlight_stubs.so
%{_libdir}/ocaml/stublibs/dllxenlight_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxentoollog_stubs.so
%{_libdir}/ocaml/stublibs/dllxentoollog_stubs.so.owner

%files devel
%{_libdir}/ocaml/xenctrl/*.a
%{_libdir}/ocaml/xenctrl/*.cmxa
%{_libdir}/ocaml/xenctrl/*.cmx
%{_libdir}/ocaml/xenctrl/*.mli
%{_libdir}/ocaml/xenlight/*.a
%{_libdir}/ocaml/xenlight/*.cmxa
%{_libdir}/ocaml/xenlight/*.cmx
%{_libdir}/ocaml/xenlight/*.mli

%files runtime
%{_libexecdir}/xenopsd/xenguest

%changelog
* Tue Sep 2 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.25-2
- Reinstate xenlight in CentOS

* Sun Aug 23 2014 David Scott <dave.scott@citrix.com> - 0.9.25-1
- Update to 0.9.25

* Sun Aug 23 2014 David Scott <dave.scott@citrix.com> - 0.9.23-1
- Update to 0.9.23, improved configure script

* Sat Aug 22 2014 David Scott <dave.scott@citrix.com> - 0.9.22-1
- Update to 0.9.22, only build xenlight on xen-4.4 and xen-4.5

* Wed Aug 20 2014 David Scott <dave.scott@citrix.com> - 0.9.21-1
- Update to 0.9.21, re-activate xenlight

* Sat Jun 21 2014 David Scott <dave.scott@citrix.com> - 0.9.18-1
- Update to 0.9.18

* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 0.9.16-2
- Place xenguest in %{name}-runtime

* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 0.9.16-1
- Update to 0.9.16

* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 0.9.15-1
- Update to 0.9.15

* Mon Jun  2 2014 Euan Harris <euan.harris@citrix.com> - 0.9.14-2
- Split files correctly between base and devel packages

* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 0.9.14-1
- Update to 0.9.14

* Mon Oct 21 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.9-3
- Exclude the xenlight stuff in case it manages to build

* Sun Oct 20 2013 David Scott <dave.scott@eu.citrix.com>
- Remove xenlight because this old version isn't enough for xenopsd-xenlight

* Mon Sep 16 2013 Euan Harris <euan.harris@citrix.com>
- Update to 0.9.9, which includes linker paths required on Debian

* Fri Jun 21 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

