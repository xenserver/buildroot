%global debug_package %{nil}

Name:           ocaml-xen-lowlevel-libs
Version:        0.9.15
Release:        1%{?dist}
Summary:        Xen hypercall bindings for OCaml
License:        LGPL
Group:          Development/Libraries
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
BuildRequires:  ocaml-cstruct-devel

%description
Xen hypercall bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make configure
./configure --disable-xenlight
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install BINDIR=%{buildroot}/var/lib/xcp/xenguest

%files
#This space intentionally left blank
/var/lib/xcp/xenguest

%files devel
%doc README.md
%{_libdir}/ocaml/xenctrl/*
#%{_libdir}/ocaml/xenlight/*
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so.owner
#%{_libdir}/ocaml/stublibs/dllxenlight_stubs.so
#%{_libdir}/ocaml/stublibs/dllxenlight_stubs.so.owner
#%{_libdir}/ocaml/stublibs/dllxentoollog_stubs.so
#%{_libdir}/ocaml/stublibs/dllxentoollog_stubs.so.owner


%changelog
* Mon May 12 2014 David Scott <dave.scott@citrix.com> - 0.9.15-1
- Update to 0.9.15

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

