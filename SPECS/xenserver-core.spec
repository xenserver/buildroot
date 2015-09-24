Name:           xenserver-core
Version:        0.10.0
Release:        4%{?dist}
Summary:        A virtual package which installs the xapi toolstack
License:        LGPL
URL:            http://www.xenserver.org/
Source0:        xenserver-readme
Requires:       xenserver-install-wizard
Requires:       xapi
Requires:       xapi-python-devel
Requires:       xapi-xe
Requires:       xenopsd-simulator
Requires:       xenopsd-xc
Requires:       xenopsd-xenlight
Requires:       xenops-cli
Requires:       ffs
Requires:       sm-cli
Requires:       xcp-sm
Requires:       xapi-storage-script
Requires:       xapi-storage-datapath-plugins
Requires:       ezlvm
Requires:       xcp-networkd
Requires:       xcp-rrdd
Requires:       squeezed
Requires:       linux-guest-loader
Requires:       xen
Requires:       busybox
%description
A virtual package which installs the xapi toolstack.

%prep
%setup -c -T
cp %{SOURCE0} xenserver-readme

%build

%install
mkdir -p %{buildroot}/usr/share/doc/xenserver
install -m 0644 xenserver-readme %{buildroot}/usr/share/doc/xenserver/README


%files
/usr/share/doc/xenserver/README

%changelog
* Fri Sep 11 2015 David Scott <dave.scott@citrix.com> - 0.10.0-4
- Add dependency on xapi-storage-datapath-plugins

* Fri Oct 17 2014 David Scott <dave.scott@citrix.com> - 0.10.0-3
- Add dependency on xapi-storage-script and ezlvm

* Wed Aug 20 2014 David Scott <dave.scott@eu.citrix.com> - 0.10.0-2
- Add dependency on xenopsd-xenlight

* Fri Nov 1 2013 Euan Harris <dave.scott@eu.citrix.com> - 0.10.0-1
- Bump version to 0.10.0

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

