Name:           xenserver-core
Version:        0.9.0
Release:        11
Summary:        A virtual package which installs the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            http://www.xen.org/
Source0:        xenserver-readme
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       xenserver-install-wizard
Requires:       xapi xapi-xe xe-create-templates xapi-python-devel
Requires:       xenopsd-xc xenopsd-libvirt xenopsd-simulator
Requires:       xenops-cli
Requires:       ffs xapi-libvirt-storage sm-cli xcp-sm
Requires:       xcp-networkd
Requires:       xcp-rrdd
Requires:       squeezed
Requires:       eliloader
Requires:       kernel >= 3.4.46 kernel-firmware
Requires:       xen

%description
A virtual package which installs the xapi toolstack.

%prep
%setup -c -T
cp %{SOURCE0} xenserver-readme

%build

%install
mkdir -p %{buildroot}/usr/share/doc/xenserver
install -m 0644 xenserver-readme %{buildroot}/usr/share/doc/xenserver/README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/doc/xenserver/README

%changelog
* Sun Oct 20 2013 David Scott <dave.scott@eu.citrix.com>
- Remove xenopsd-xenlight since the build depends on xen-4.4

* Fri Sep 20 2013 Euan Harris <euan.harris@citrix.com>
- Don't install openstack-xapi-plugins with xenserver-core

* Fri Jun 21 2013 David Scott <dave.scott@eu.citrix.com>
- Include xenopsd-xenlight

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- add a dependency on xcp-rrdd

* Sat Jun  8 2013 David Scott <dave.scott@eu.citrix.com>
- add a xenserver-install-wizard
- add dependency on xapi-python-devel for use by the install wizard
- include the xenops and SM CLIs

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

