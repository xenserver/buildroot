Name:           xapi-libvirt-storage
Version:        0.9.1
Release:        0
Summary:        Allows the manipulation of libvirt storage pools and volumes via xapi
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xapi-libvirt-storage/archive/xapi-libvirt-storage-%{version}.tar.gz
Source0:        https://github.com/xen-org/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        xapi-libvirt-storage-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel ocaml-libvirt-devel libvirt-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-oclock-devel

%description
Allows the manipulation of libvirt storage pools and volumes via xapi.

%prep
%setup -q -n xapi-libvirt-storage-xapi-libvirt-storage-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/sm-libvirt/sm-libvirt %{buildroot}/%{_sbindir}/xapi-libvirt-storage
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/xapi-libvirt-storage-init %{buildroot}%{_sysconfdir}/init.d/xapi-libvirt-storage

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
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

