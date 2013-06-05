Name:           xenserver
Version:        0.9.0
Release:        0
Summary:        A virtual package which installs the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            http://www.xen.org/
Source0:        xenserver-readme
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       xapi xapi-xe
Requires:       xenopsd-xc xenopsd-libvirt xenopsd-simulator
Requires:       ffs xapi-libvirt-storage
Requires:       xcp-networkd
Requires:       squeezed
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
* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

