%global debug_package %{nil}

Name:           ocaml-netdev
Version:        0.9.1
Release:        2%{?dist}
Summary:        Manipulate Linux bridges, network devices and openvswitch instances in OCaml
License:        LGPL
URL:            https://github.com/xapi-project/netdev
Source0:        https://github.com/xapi-project/netdev/archive/v%{version}/netdev-%{version}.tar.gz
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdext-devel

%description
Manipulate Linux bridges, network devices and openvswitch instances in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  forkexecd-devel%{?_isa}
BuildRequires:  ocaml-stdext-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n netdev-%{version}

%build
./configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{_libdir}/ocaml/netdev
%exclude %{_libdir}/ocaml/netdev/*.a
%exclude %{_libdir}/ocaml/netdev/*.cmxa
%exclude %{_libdir}/ocaml/netdev/*.cmx
%exclude %{_libdir}/ocaml/netdev/*.mli
%{_libdir}/ocaml/stublibs/dllnetdev_stubs.so
%{_libdir}/ocaml/stublibs/dllnetdev_stubs.so.owner

%files devel
%{_libdir}/ocaml/netdev/*.a
%{_libdir}/ocaml/netdev/*.cmx
%{_libdir}/ocaml/netdev/*.cmxa
%{_libdir}/ocaml/netdev/*.mli

%changelog
* Wed Sep 9 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-2
- Bump release

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

