Name:           xapi-libvirt-storage
Version:        0.9.7
Release:        1%{?dist}
Summary:        Allows the manipulation of libvirt storage pools and volumes via xapi
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xapi-libvirt-storage/archive/%{version}.tar.gz
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xapi-libvirt-storage-init
BuildRequires:  libvirt-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-libvirt-devel
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  cmdliner-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  message-switch-devel
Requires:       redhat-lsb-core

%description
Allows the manipulation of libvirt storage pools and volumes via xapi.

%prep
%setup -q
cp %{SOURCE1} xapi-libvirt-storage-init

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/sm-libvirt/sm-libvirt %{buildroot}/%{_sbindir}/xapi-libvirt-storage
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xapi-libvirt-storage-init %{buildroot}%{_sysconfdir}/init.d/xapi-libvirt-storage


%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xapi-libvirt-storage
%{_sysconfdir}/init.d/xapi-libvirt-storage

%post
/sbin/chkconfig --add xapi-libvirt-storage

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xapi-libvirt-storage stop > /dev/null 2>&1
  /sbin/chkconfig --del xapi-libvirt-storage
fi

%changelog
* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.7-1
- Update to 0.9.7

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

