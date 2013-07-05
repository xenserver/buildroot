Name:           openstack-xapi-plugins
Version:        2013.1.2
Release:        1
Summary:        XenAPI plugins from OpenStack
License:        ASL 2.0
Group:          System/Hypervisor
URL:            https://launchpad.net/nova/grizzly/%{version}/+download/nova-%{version}.tar.gz
Source0:        https://launchpad.net/nova/grizzly/%{version}/+download/nova-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/nova-%{version}-%{release}

%define debug_package %{nil}

%description
XenAPI plugins used by OpenStack to control XenServer.

%prep
%setup -q -n nova-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}
cp -r plugins/xenserver/xenapi/etc/xapi.d %{buildroot}/%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,-)
%{_sysconfdir}/xapi.d/

%changelog
* Fri Jun 28 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

