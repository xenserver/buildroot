Name:           xenserver-core
Version:        0.9.0
Release:        8
Summary:        A virtual package which installs the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            http://www.xen.org/
Source0:        xenserver-readme
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       xenserver-install-wizard
Requires:       xapi xapi-xe xe-create-templates xapi-python-devel
Requires:       xenopsd-xc xenopsd-libvirt xenopsd-xenlight xenopsd-simulator
Requires:       xenops-cli
Requires:       ffs xapi-libvirt-storage sm-cli
Requires:       xcp-networkd
Requires:       xcp-rrdd
Requires:       squeezed
Requires:       eliloader
Requires:       kernel >= 3.4.46 kernel-firmware
Requires:       xen

%description
A virtual package which installs the xapi toolstack.

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/doc/xenserver
install -m 0644 %{_sourcedir}/xenserver-readme %{buildroot}/usr/share/doc/xenserver/README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/doc/xenserver/README

%changelog
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

