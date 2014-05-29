%global debug_package %{nil}

Name:           ocaml-netdev
Version:        0.9.0
Release:        1%{?dist}
Summary:        Manipulate Linux bridges, network devices and openvswitch instances in OCaml
License:        LGPL
URL:            https://github.com/xapi-project/netdev
Source0:        https://github.com/xapi-project/netdev/archive/netdev-%{version}/netdev-%{version}.tar.gz
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
%setup -q -n netdev-netdev-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/netdev/*
%{_libdir}/ocaml/stublibs/dllnetdev_stubs.so
%{_libdir}/ocaml/stublibs/dllnetdev_stubs.so.owner

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

