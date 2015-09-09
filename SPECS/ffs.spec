Name:           ffs
Version:        0.26
Release:        1%{?dist}
Summary:        Simple flat file storage manager for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/ffs
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       xapi-storage

%description
Simple flat file storage manager for the xapi toolstack.

%prep
%setup -q

%build

%install
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script/ PYTHONDIR=/usr/lib/python2.7/site-packages/xapi make install

%files
%doc README.md LICENSE MAINTAINERS
%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.ffs/*
%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.btrfs/*
%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.rawnfs/*
%{_libexecdir}/xapi-storage-script/datapath/raw+file
%{_libexecdir}/xapi-storage-script/datapath/vhd+file
%{_libexecdir}/xapi-storage-script/datapath/loop+blkback/*
%{_libexecdir}/xapi-storage-script/datapath/tapdisk/*
/usr/lib/python2.7/site-packages/xapi/*.py*
/etc/xapi.d/plugins/ffs

%changelog
* Wed Sep 09 2015 David Scott <dave.scott@citrix.com> - 0.26-1
- Update to 0.26

* Wed Aug 05 2015 David Scott <dave.scott@citrix.com> - 0.25-1
- Update to 0.25

* Mon Jul 20 2015 David Scott <dave.scott@citrix.com> - 0.24-1
- Update to 0.24

* Wed Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.23-1
- Update to 0.23

* Mon Jul 13 2015 David Scott <dave.scott@citrix.com> - 0.22-1
- Update to 0.22

* Sat Jul 11 2015 David Scott <dave.scott@citrix.com> - 0.21-1
- Update to 0.21

* Fri Jul 10 2015 David Scott <dave.scott@citrix.com> - 0.20-1
- Update to 0.20

* Thu Jul 9 2015 David Scott <dave.scott@citrix.com> - 0.19-1
- Update to 0.19

* Thu Jul 9 2015 David Scott <dave.scott@citrix.com> - 0.17-1
- Update to 0.17

* Thu Jul 9 2015 David Scott <dave.scott@citrix.com> - 0.16-1
- Update to 0.16

* Wed Jul 8 2015 David Scott <dave.scott@citrix.com> - 0.15-1
- Update to 0.15

* Wed Jul 8 2015 David Scott <dave.scott@citrix.com> - 0.14-1
- Update to 0.14

* Mon Jul 6 2015 David Scott <dave.scott@citrix.com> - 0.13-1
- Update to 0.13

* Mon Jul 6 2015 David Scott <dave.scott@citrix.com> - 0.12-1
- Update to 0.12

* Tue Jun 16 2015 David Scott <dave.scott@citrix.com> - 0.11-2
- Hack to install python files in the right place

* Tue Jun 9 2015 David Scott <dave.scott@citrix.com> - 0.11-1
- Update to 0.11

* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.9.25-1
- Update to 0.9.25

* Thu Jan 16 2014 Euan Harris <euan.harris@citrix.com> - 0.9.24-1
- Update to 0.9.24, with VDI.clone fix

* Thu Oct 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.23-1
- Update to 0.9.23, with VDI.copy fix

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.22, with VDI.clone and VDI.snapshot fixes

* Mon Oct 28 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.21, with minimal storage motion support

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.20
- Detect a parallel install of blktap and use that

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.18

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.17

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.4

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

