Summary: Bootloader for EL-based distros that support Xen
Name: eliloader
Version: 0.3
Release: 1
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
