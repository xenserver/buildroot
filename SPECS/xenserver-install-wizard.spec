# -*- rpm-spec -*-

Summary: a simple wizard to configure a XenServer
Name:    xenserver-install-wizard
Version: 0.1.0
Release: 0
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://github.com/djs55/xenserver-install-wizard
Source0: xenserver-install-wizard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python whiptail xapi-python-devel

%description
A simple wizard to configure a XenServer after install

%prep 
%setup -q -n xenserver-install-wizard-%{version}

%build

%install
make DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_bindir}
ln -s /usr/share/xenserver-install-wizard/xenserver-install-wizard.py %{buildroot}%{_bindir}/xenserver-install-wizard

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/xenserver-install-wizard/*
%{_bindir}/xenserver-install-wizard

%changelog
* Sun Jun 8 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package






