%global debug_package %{nil}

Name:           ocaml-fd-send-recv
Version:        1.0.1
Release:        2%{?dist}
Summary:        Bindings to sendmsg/recvmsg for fd passing under Linux
License:        LGPL
URL:            https://github.com/xapi-project/ocaml-fd-send-recv
Source0:        https://github.com/xapi-project/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
Bindings to sendmsg/recvmsg for fd passing under Linux.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install

%files
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/fd-send-recv
%exclude %{_libdir}/ocaml/fd-send-recv/*.a
%exclude %{_libdir}/ocaml/fd-send-recv/*.cmxa
%exclude %{_libdir}/ocaml/fd-send-recv/*.cmx
%exclude %{_libdir}/ocaml/fd-send-recv/*.mli
%{_libdir}/ocaml/stublibs/dllfd_send_recv_stubs.so
%{_libdir}/ocaml/stublibs/dllfd_send_recv_stubs.so.owner

%files devel
%{_libdir}/ocaml/fd-send-recv/*.a
%{_libdir}/ocaml/fd-send-recv/*.cmx
%{_libdir}/ocaml/fd-send-recv/*.cmxa
%{_libdir}/ocaml/fd-send-recv/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.0.1-2
- Split files correctly between base and devel packages

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.0.1-1
- Initial package

