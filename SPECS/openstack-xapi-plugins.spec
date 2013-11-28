Name:           openstack-xapi-plugins
Version:        2013.2
Release:        1
Summary:        XenAPI plugins from OpenStack
License:        ASL 2.0
Group:          System/Hypervisor
URL:            https://launchpad.net/nova/havana
Source0:        https://launchpad.net/nova/havana/%{version}/+download/nova-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/nova-%{version}-%{release}
BuildRequires:  python-setuptools

%define debug_package %{nil}

%description
XenAPI plugins used by OpenStack to control XenServer.

%prep
%setup -q -n nova-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/xapi/plugins
cp -r plugins/xenserver/xenapi/etc/xapi.d/plugins/* %{buildroot}/usr/lib/xapi/plugins/

%build
#This space intentionally left blank

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,-)
/usr/lib/xapi/plugins/*

%changelog
* Wed Nov 20 2013 Euan Harris <euan.harris@citrix.com> - 2013.2-1
- Update to Havana release

* Wed Jul  3 2013 David Scott <dave.scott@eu.citrix.com>
- Tweak plugins directory to match xapi

* Fri Jun 28 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

