Name:           ocaml-netlink
Version:        0.1.0
Release:        1%{?dist}
Summary:        OCaml bindings to libnl
License:        LGPL
URL:            https://github.com/xapi-project/ocaml-netlink
Source0:        https://github.com/xapi-project/ocaml-netlink/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libffi-devel
BuildRequires:  libnl3
BuildRequires:  ocaml
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild

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
* Thu Jun 05 2014 Rob Hoes <rob.hoes@citrix.com> - 0.1.0-1
- Initial package

