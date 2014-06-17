# -*- rpm-spec -*-

Summary: A simple wizard to configure a XenServer
Name:    xenserver-install-wizard
Version: 0.2.32
Release: 1%{?dist}
License: LGPL+linking exception
URL:  https://github.com/xenserver/xenserver-install-wizard
Source0: https://github.com/xenserver/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: xenserver-install-wizard-init
Requires: newt
Requires: python
Requires: python-argparse
Requires: xapi-python-devel

%description
A simple wizard to configure a XenServer after install

%prep 
%setup -q
cp %{SOURCE1} xenserver-install-wizard-init

%build

%install
make DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_bindir}
ln -s /usr/share/xenserver-install-wizard/xenserver-install-wizard.py %{buildroot}%{_bindir}/xenserver-install-wizard
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xenserver-install-wizard-init %{buildroot}%{_sysconfdir}/init.d/xenserver-install-wizard

%files
/usr/share/xenserver-install-wizard/*
%{_bindir}/xenserver-install-wizard
%{_sysconfdir}/init.d/xenserver-install-wizard

%post
[ ! -x /sbin/chkconfig ] || chkconfig --add xenserver-install-wizard

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xenserver-install-wizard stop > /dev/null 2>&1
  /sbin/chkconfig --del xenserver-install-wizard
fi

%changelog
* Tue Jun 17 2014 David Scott <dave.scott@citrix.com> - 0.2.32-1
- Add init script
- Update to 0.2.32

* Sat May 10 2014 David Scott <dave.scott@citrix.com> - 0.2.30-1
- Update to 0.2.30, now starts xcp-rrdd

* Tue Apr 29 2014 Bob Ball <bob.ball@citrix.com> - 0.2.29-1
- Update to 0.2.29, with fixes for static IP on debian/ubuntu

* Wed Jan 15 2014 Euan Harris <euan.harris@citrix.com> - 0.2.28-2
- Source moved to https://github.com/xenserver/xenserver-install-wizard

* Wed Dec 4 2013 Euan Harris <euan.harris@citrix.com> - 0.2.28-1
- Update to 0.2.28, with fixes for RHEL

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

* Mon Sep  2 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.18

* Mon Jun 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.4

* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.2.0, hopefully the first fully-working version

* Sat Jun  8 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

