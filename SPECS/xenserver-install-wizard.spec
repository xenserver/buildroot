# -*- rpm-spec -*-

Summary: a simple wizard to configure a XenServer
Name:    xenserver-install-wizard
Version: 0.2.16
Release: 0
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://github.com/djs55/xenserver-install-wizard
Source0: https://github.com/djs55/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python newt xapi-python-devel

%description
A simple wizard to configure a XenServer after install

%prep 
%setup -q

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
* Mon Jun 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.4

* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.0, hopefully the first fully-working version

* Sat Jun  8 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package






