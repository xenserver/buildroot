Summary: Bootloader for EL-based distros that support Xen
Name: eliloader
Version: 0.3
Release: 1
URL: https://github.com/djs55/xcp-eliloader
Source0: https://github.com/djs55/xcp-%{name}/archive/master/%{version}/%{name}-%{version}.tar.gz
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
 
%description
Bootloader for EL-based distros that support Xen.

%prep
%setup -q -n xcp-%{name}-master-%{version}

%build
 
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 eliloader.py %{buildroot}%{_sbindir}/eliloader

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/eliloader

%changelog
* Mon Jun 24 2013 David Scott <dave.scott@eu.citrix.com> - 0.3-1
- Update to eliloader 0.3

* Sat Jun 22 2013 David Scott <dave.scott@eu.citrix.com> - 0.2-1
- Update to eliloader 0.2 (doesn't assume data file directory is present)

* Sat Jun 22 2013 David Scott <dave.scott@eu.citrix.com> - 0.1-1
- Initial package

