# -*- rpm-spec -*-

Summary: A simple wizard to configure a XenServer
Name:    xenserver-install-wizard
Version: 0.2.27
Release: 1
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://github.com/djs55/xenserver-install-wizard
Source0: https://github.com/djs55/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python newt xapi-python-devel python-argparse

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
* Wed Oct 30 2013 Euan Harris <euan.harris@citrix.com> - 0.2.27-1
- Update to 0.2.27

* Thu Oct 24 2013 Euan Harris <euan.harris@citrix.com>
- Update to 0.2.26, which sets the iSCSI QN

* Thu Sep 26 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.25

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.24

* Fri Sep 20 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.23

* Wed Sep 11 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.20

* Mon Sep  2 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.19

* Mon Sep  1 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.18

* Mon Jun 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.4

* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.0, hopefully the first fully-working version

* Sat Jun  8 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package






