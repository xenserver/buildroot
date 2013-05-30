Name:           ocaml-netdev
Version:        0.9.0
Release:        0
Summary:        Manipulate Linux bridges, network devices and openvswitch instances in OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/netdev/archive/netdev-0.9.0.tar.gz
Source0:        netdev-0.9.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
# forkexec stdext
Requires:       ocaml ocaml-findlib

%description
Manipulate Linux bridges, network devices and openvswitch instances in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n netdev-netdev-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/netdev/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

