Name:           openstack-xapi-plugins
Version:        2014.1
Release:        1%{?dist}
Summary:        XenAPI plugins from OpenStack
License:        ASL 2.0
URL:            https://launchpad.net/nova/icehouse
Source0:        https://launchpad.net/nova/icehouse/%{version}/+download/nova-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-setuptools

%define debug_package %{nil}

%description
XenAPI plugins used by OpenStack to control XenServer.

%prep
%setup -q -n nova-%{version}

%build
# This package does not have a build step 

%install
mkdir -p %{buildroot}/usr/lib/xapi/plugins
cp -r plugins/xenserver/xenapi/etc/xapi.d/plugins/* %{buildroot}/usr/lib/xapi/plugins/

%files
/usr/lib/xapi/plugins/*

%changelog
* Thu May 22 2014 Antony Messerli <amesserl@rackspace.com> - 2014.1-1
- Update to Icehouse release

* Wed Nov 20 2013 Euan Harris <euan.harris@citrix.com> - 2013.2-1
- Update to Havana release

* Wed Jul  3 2013 David Scott <dave.scott@eu.citrix.com>
- Tweak plugins directory to match xapi

* Fri Jun 28 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

