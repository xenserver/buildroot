Name:           ocaml-netlink
Version:        0.2.1
Release:        1%{?dist}
Summary:        OCaml bindings to libnl
License:        LGPL
URL:            https://github.com/xapi-project/ocaml-netlink
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  libffi-devel
BuildRequires:  libnl3
BuildRequires:  ocaml
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  ocaml-findlib

%description
The Netlink Protocol Library Suite (libnl) provides APIs to the netlink
protocol, allowing you to interact with network devices in the Linux kernel.
This library provides OCaml bindings to libnl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-ctypes-devel%{?_isa}
Requires:       libffi%{?_isa}
Requires:       libnl3%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%files
%doc README.md
%{_libdir}/ocaml/netlink
%exclude %{_libdir}/ocaml/netlink/*.a
%exclude %{_libdir}/ocaml/netlink/*.cmxa
%exclude %{_libdir}/ocaml/netlink/*.cmx

%files devel
%{_libdir}/ocaml/netlink/*.a
%{_libdir}/ocaml/netlink/*.cmx
%{_libdir}/ocaml/netlink/*.cmxa

%changelog
* Thu Apr 23 2015 Euan Harris <euan.harris@citrix.com> - 0.2.1-1
- Update to 0.2.1

* Wed Oct 01 2014 David Scott <dave.scott@citrix.com> - 0.2.0-1
- Update to 0.2.0

* Thu Jun 05 2014 Rob Hoes <rob.hoes@citrix.com> - 0.1.0-1
- Initial package

