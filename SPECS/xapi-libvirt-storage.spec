Name:           xapi-libvirt-storage
Version:        0.9.7
Release:        1
Summary:        Allows the manipulation of libvirt storage pools and volumes via xapi
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xapi-libvirt-storage/archive/%{version}.tar.gz
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xapi-libvirt-storage-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel ocaml-libvirt-devel libvirt-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/sm-libvirt/sm-libvirt %{buildroot}/%{_sbindir}/xapi-libvirt-storage
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xapi-libvirt-storage-init %{buildroot}%{_sysconfdir}/init.d/xapi-libvirt-storage

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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

