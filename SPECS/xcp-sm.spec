# -*- rpm-spec -*-

Summary: XCP storage managers
Name:    xcp-sm
Version: 0.9.8
Release: 1%{?dist}
License: LGPL
URL:  https://github.com/xapi-project/sm
Source0: https://github.com/xapi-project/sm/archive/creedence-alpha-4/sm-%{version}.tar.gz
Source1: xcp-mpath-scsidev-rules
Source2: xcp-mpath-scsidev-script
Patch0: xcp-sm-scsi-id-path.patch
Patch1: xcp-sm-pylint-fix.patch
Patch2: xcp-sm-path-fix.patch
Patch3: xcp-sm-pidof-path.patch
Patch4: xcp-sm-initiator-name.patch
BuildRequires: python-devel
BuildRequires: swig
BuildRequires: xen-devel
BuildRequires: pylint
Requires: iscsi-initiator-utils
Requires: sg3_utils
Requires: xen-runtime

%description
This package contains storage backends used in XCP

%prep
%setup -q -n sm-creedence-alpha-4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cp %{SOURCE1} xcp-mpath-scsidev-rules
cp %{SOURCE2} xcp-mpath-scsidev-script

%build
DESTDIR=$RPM_BUILD_ROOT make

%install
make PLUGIN_SCRIPT_DEST=%{_libdir}/xapi/plugins/ SM_DEST=%{_libdir}/xapi/sm/ BLKTAP_ROOT=%{_libdir}/blktap INVENTORY=/etc/xcp/inventory DESTDIR=$RPM_BUILD_ROOT install
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 xcp-mpath-scsidev-rules %{buildroot}/etc/udev/rules.d/55-xs-mpath-scsidev.rules
mkdir -p %{buildroot}/etc/udev/scripts
install -m 0755 xcp-mpath-scsidev-script %{buildroot}/etc/udev/scripts/xs-mpath-scsidev.sh


%post
[ ! -x /sbin/chkconfig ] || chkconfig --add mpathroot
[ ! -x /sbin/chkconfig ] || chkconfig --add sm-multipath
service sm-multipath start

[ -f /etc/lvm/lvm.conf.orig ] || cp /etc/lvm/lvm.conf /etc/lvm/lvm.conf.orig || exit $?
[ -d /etc/lvm/master ] || mkdir /etc/lvm/master || exit $?
mv -f /etc/lvm/lvm.conf /etc/lvm/master/lvm.conf || exit $?
sed -i 's/metadata_read_only =.*/metadata_read_only = 0/' /etc/lvm/master/lvm.conf || exit $?
sed -i 's/archive = .*/archive = 0/' /etc/lvm/master/lvm.conf || exit $?
sed -i 's/filter \= \[ \"a\/\.\*\/\" \]/filter = \[ \"r\|\/dev\/xvd\.\|\"\, \"r\|\/dev\/VG\_Xen\.\*\/\*\|\"\]/g' /etc/lvm/master/lvm.conf || exit $?
cp /etc/lvm/master/lvm.conf /etc/lvm/lvm.conf || exit $?
sed -i 's/metadata_read_only =.*/metadata_read_only = 1/' /etc/lvm/lvm.conf || exit $?
# We try to be "update-alternatives" ready.
# If a file exists and it is not a symlink we back it up
if [ -e /etc/multipath.conf -a ! -h /etc/multipath.conf ]; then
   mv -f /etc/multipath.conf /etc/multipath.conf.$(date +%F_%T)
fi
update-alternatives --install /etc/multipath.conf multipath.conf /etc/multipath.xenserver/multipath.conf 90

%preun
[ ! -x /sbin/chkconfig ] || chkconfig --del sm-multipath
#only remove in case of erase (but not at upgrade)
if [ $1 -eq 0 ] ; then
   update-alternatives --remove multipath.conf /etc/multipath.xenserver/multipath.conf
fi
exit 0

%postun
[ ! -d /etc/lvm/master ] || rm -Rf /etc/lvm/master || exit $?
cp -f /etc/lvm/lvm.conf.orig /etc/lvm/lvm.conf || exit $?

%files
/etc/cron.d/*
/etc/rc.d/init.d/snapwatchd
/etc/rc.d/init.d/mpathroot
/etc/rc.d/init.d/sm-multipath
/etc/udev/rules.d/55-xs-mpath-scsidev.rules
/etc/udev/scripts/xs-mpath-scsidev.sh
%{_libdir}/xapi/plugins/coalesce-leaf
%{_libdir}/xapi/plugins/lvhd-thin
%{_libdir}/xapi/plugins/nfs-on-slave
%{_libdir}/xapi/plugins/on-slave
%{_libdir}/xapi/plugins/tapdisk-pause
%{_libdir}/xapi/plugins/testing-hooks
%{_libdir}/xapi/plugins/vss_control
%{_libdir}/xapi/plugins/intellicache-clean
/etc/xensource/master.d/02-vhdcleanup
/opt/xensource/bin/blktap2
/opt/xensource/bin/tapdisk-cache-stats
/opt/xensource/debug/tp
/opt/xensource/libexec/check-device-sharing
/opt/xensource/libexec/dcopy
/opt/xensource/libexec/local-device-change
%{_libdir}/xapi/sm/DummySR
%{_libdir}/xapi/sm/DummySR.py
%{_libdir}/xapi/sm/DummySR.pyc
%{_libdir}/xapi/sm/DummySR.pyo
%{_libdir}/xapi/sm/EXTSR
%{_libdir}/xapi/sm/EXTSR.py
%{_libdir}/xapi/sm/EXTSR.pyc
%{_libdir}/xapi/sm/EXTSR.pyo
%{_libdir}/xapi/sm/FileSR
%{_libdir}/xapi/sm/FileSR.py
%{_libdir}/xapi/sm/FileSR.pyc
%{_libdir}/xapi/sm/FileSR.pyo
%{_libdir}/xapi/sm/HBASR
%{_libdir}/xapi/sm/HBASR.py
%{_libdir}/xapi/sm/HBASR.pyc
%{_libdir}/xapi/sm/HBASR.pyo
%{_libdir}/xapi/sm/ISCSISR
%{_libdir}/xapi/sm/ISCSISR.py
%{_libdir}/xapi/sm/ISCSISR.pyc
%{_libdir}/xapi/sm/ISCSISR.pyo
%{_libdir}/xapi/sm/ISOSR
%{_libdir}/xapi/sm/ISOSR.py
%{_libdir}/xapi/sm/ISOSR.pyc
%{_libdir}/xapi/sm/ISOSR.pyo
%{_libdir}/xapi/sm/OCFSSR.py
%{_libdir}/xapi/sm/OCFSSR.pyc
%{_libdir}/xapi/sm/OCFSSR.pyo
%{_libdir}/xapi/sm/OCFSoISCSISR
%{_libdir}/xapi/sm/OCFSoISCSISR.py
%{_libdir}/xapi/sm/OCFSoISCSISR.pyc
%{_libdir}/xapi/sm/OCFSoISCSISR.pyo
%{_libdir}/xapi/sm/OCFSoHBASR
%{_libdir}/xapi/sm/OCFSoHBASR.py
%{_libdir}/xapi/sm/OCFSoHBASR.pyc
%{_libdir}/xapi/sm/OCFSoHBASR.pyo
%{_libdir}/xapi/sm/LUNperVDI.py
%{_libdir}/xapi/sm/LUNperVDI.pyc
%{_libdir}/xapi/sm/LUNperVDI.pyo
%{_libdir}/xapi/sm/LVHDSR.py
%{_libdir}/xapi/sm/LVHDSR.pyc
%{_libdir}/xapi/sm/LVHDSR.pyo
%{_libdir}/xapi/sm/LVHDoHBASR.py
%{_libdir}/xapi/sm/LVHDoHBASR.pyc
%{_libdir}/xapi/sm/LVHDoHBASR.pyo
%{_libdir}/xapi/sm/LVHDoISCSISR.py
%{_libdir}/xapi/sm/LVHDoISCSISR.pyc
%{_libdir}/xapi/sm/LVHDoISCSISR.pyo
%{_libdir}/xapi/sm/LVMSR
%{_libdir}/xapi/sm/LVMoHBASR
%{_libdir}/xapi/sm/LVMoISCSISR
%{_libdir}/xapi/sm/NFSSR
%{_libdir}/xapi/sm/NFSSR.py
%{_libdir}/xapi/sm/NFSSR.pyc
%{_libdir}/xapi/sm/NFSSR.pyo
%{_libdir}/xapi/sm/SHMSR.py
%{_libdir}/xapi/sm/SHMSR.pyc
%{_libdir}/xapi/sm/SHMSR.pyo
%{_libdir}/xapi/sm/SR.py
%{_libdir}/xapi/sm/SR.pyc
%{_libdir}/xapi/sm/SR.pyo
%{_libdir}/xapi/sm/SRCommand.py
%{_libdir}/xapi/sm/SRCommand.pyc
%{_libdir}/xapi/sm/SRCommand.pyo
%{_libdir}/xapi/sm/VDI.py
%{_libdir}/xapi/sm/VDI.pyc
%{_libdir}/xapi/sm/VDI.pyo
%{_libdir}/xapi/sm/XE_SR_ERRORCODES.xml
%{_libdir}/xapi/sm/blktap2.py
%{_libdir}/xapi/sm/blktap2.pyc
%{_libdir}/xapi/sm/blktap2.pyo
%{_libdir}/xapi/sm/constants.py
%{_libdir}/xapi/sm/constants.pyc
%{_libdir}/xapi/sm/constants.pyo
%{_libdir}/xapi/sm/cleanup.py
%{_libdir}/xapi/sm/cleanup.pyc
%{_libdir}/xapi/sm/cleanup.pyo
%{_libdir}/xapi/sm/devscan.py
%{_libdir}/xapi/sm/devscan.pyc
%{_libdir}/xapi/sm/devscan.pyo
%{_libdir}/xapi/sm/fjournaler.py
%{_libdir}/xapi/sm/fjournaler.pyc
%{_libdir}/xapi/sm/fjournaler.pyo
%{_libdir}/xapi/sm/flock.py
%{_libdir}/xapi/sm/flock.pyc
%{_libdir}/xapi/sm/flock.pyo
%{_libdir}/xapi/sm/ipc.py
%{_libdir}/xapi/sm/ipc.pyc
%{_libdir}/xapi/sm/ipc.pyo
%{_libdir}/xapi/sm/iscsilib.py
%{_libdir}/xapi/sm/iscsilib.pyc
%{_libdir}/xapi/sm/iscsilib.pyo
%{_libdir}/xapi/sm/journaler.py
%{_libdir}/xapi/sm/journaler.pyc
%{_libdir}/xapi/sm/journaler.pyo
%{_libdir}/xapi/sm/lcache.py
%{_libdir}/xapi/sm/lcache.pyc
%{_libdir}/xapi/sm/lcache.pyo
%{_libdir}/xapi/sm/lock.py
%{_libdir}/xapi/sm/lock.pyc
%{_libdir}/xapi/sm/lock.pyo
%{_libdir}/xapi/sm/lvhdutil.py
%{_libdir}/xapi/sm/lvhdutil.pyc
%{_libdir}/xapi/sm/lvhdutil.pyo
%{_libdir}/xapi/sm/lvmanager.py
%{_libdir}/xapi/sm/lvmanager.pyc
%{_libdir}/xapi/sm/lvmanager.pyo
%{_libdir}/xapi/sm/lvmcache.py
%{_libdir}/xapi/sm/lvmcache.pyc
%{_libdir}/xapi/sm/lvmcache.pyo
%{_libdir}/xapi/sm/lvutil.py
%{_libdir}/xapi/sm/lvutil.pyc
%{_libdir}/xapi/sm/lvutil.pyo
%{_libdir}/xapi/sm/metadata.py
%{_libdir}/xapi/sm/metadata.pyc
%{_libdir}/xapi/sm/metadata.pyo
%{_libdir}/xapi/sm/srmetadata.py
%{_libdir}/xapi/sm/srmetadata.pyc
%{_libdir}/xapi/sm/srmetadata.pyo
%{_libdir}/xapi/sm/mpath_cli.py
%{_libdir}/xapi/sm/mpath_cli.pyc
%{_libdir}/xapi/sm/mpath_cli.pyo
%{_libdir}/xapi/sm/mpath_dmp.py
%{_libdir}/xapi/sm/mpath_dmp.pyc
%{_libdir}/xapi/sm/mpath_dmp.pyo
%{_libdir}/xapi/sm/mpath_null.py
%{_libdir}/xapi/sm/mpath_null.pyc
%{_libdir}/xapi/sm/mpath_null.pyo
%{_libdir}/xapi/sm/mpathcount.py
%{_libdir}/xapi/sm/mpathcount.pyc
%{_libdir}/xapi/sm/mpathcount.pyo
%{_libdir}/xapi/sm/mpathutil.py
%{_libdir}/xapi/sm/mpathutil.pyc
%{_libdir}/xapi/sm/mpathutil.pyo
%{_libdir}/xapi/sm/mpp_luncheck.py
%{_libdir}/xapi/sm/mpp_luncheck.pyc
%{_libdir}/xapi/sm/mpp_luncheck.pyo
%{_libdir}/xapi/sm/mpp_mpathutil.py
%{_libdir}/xapi/sm/mpp_mpathutil.pyc
%{_libdir}/xapi/sm/mpp_mpathutil.pyo
%{_libdir}/xapi/sm/nfs.py
%{_libdir}/xapi/sm/nfs.pyc
%{_libdir}/xapi/sm/nfs.pyo
%{_libdir}/xapi/sm/refcounter.py
%{_libdir}/xapi/sm/refcounter.pyc
%{_libdir}/xapi/sm/refcounter.pyo
%{_libdir}/xapi/sm/resetvdis.py
%{_libdir}/xapi/sm/resetvdis.pyc
%{_libdir}/xapi/sm/resetvdis.pyo
%{_libdir}/xapi/sm/scsiutil.py
%{_libdir}/xapi/sm/scsiutil.pyc
%{_libdir}/xapi/sm/scsiutil.pyo
%{_libdir}/xapi/sm/scsi_host_rescan.py
%{_libdir}/xapi/sm/scsi_host_rescan.pyc
%{_libdir}/xapi/sm/scsi_host_rescan.pyo
%{_libdir}/xapi/sm/snapwatchd/snapwatchd
%{_libdir}/xapi/sm/snapwatchd/xslib.py
%{_libdir}/xapi/sm/snapwatchd/xslib.pyc
%{_libdir}/xapi/sm/snapwatchd/xslib.pyo
%{_libdir}/xapi/sm/snapwatchd/snapdebug.py
%{_libdir}/xapi/sm/snapwatchd/snapdebug.pyc
%{_libdir}/xapi/sm/snapwatchd/snapdebug.pyo
%{_libdir}/xapi/sm/sysdevice.py
%{_libdir}/xapi/sm/sysdevice.pyc
%{_libdir}/xapi/sm/sysdevice.pyo
%{_libdir}/xapi/sm/udevSR
%{_libdir}/xapi/sm/udevSR.py
%{_libdir}/xapi/sm/udevSR.pyc
%{_libdir}/xapi/sm/udevSR.pyo
%{_libdir}/xapi/sm/updatempppathd.py
%{_libdir}/xapi/sm/updatempppathd.pyc
%{_libdir}/xapi/sm/updatempppathd.pyo
%{_libdir}/xapi/sm/util.py
%{_libdir}/xapi/sm/util.pyc
%{_libdir}/xapi/sm/util.pyo
%{_libdir}/xapi/sm/verifyVHDsOnSR.py
%{_libdir}/xapi/sm/verifyVHDsOnSR.pyc
%{_libdir}/xapi/sm/verifyVHDsOnSR.pyo
%{_libdir}/xapi/sm/vhdutil.py
%{_libdir}/xapi/sm/vhdutil.pyc
%{_libdir}/xapi/sm/vhdutil.pyo
%{_libdir}/xapi/sm/vss_control
%{_libdir}/xapi/sm/xs_errors.py
%{_libdir}/xapi/sm/xs_errors.pyc
%{_libdir}/xapi/sm/xs_errors.pyo
%{_libdir}/xapi/sm/wwid_conf.py
%{_libdir}/xapi/sm/wwid_conf.pyc
%{_libdir}/xapi/sm/wwid_conf.pyo
/sbin/mpathutil
%config /etc/udev/rules.d/40-multipath.rules
%config /etc/multipath.xenserver/multipath.conf


%package rawhba
Summary: XCP rawhba SR type capability
#Requires: sm = @SM_VERSION@-@SM_RELEASE@

%description rawhba
This package adds a new rawhba SR type. This SR type allows utilization of
Fiber Channel raw LUNs as separate VDIs (LUN per VDI)

%files rawhba
%{_libdir}/xapi/sm/RawHBASR
%{_libdir}/xapi/sm/RawHBASR.py
%{_libdir}/xapi/sm/RawHBASR.pyc
%{_libdir}/xapi/sm/RawHBASR.pyo
%{_libdir}/xapi/sm/B_util.py
%{_libdir}/xapi/sm/B_util.pyc
%{_libdir}/xapi/sm/B_util.pyo

%changelog
* Tue Sep 30 2014 Bob Ball <bob.ball@citrix.com> - 0.9.8-1
- Moved patches to spec file rather than custom repository

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-3
- Remove xen-missing-headers dependency

* Fri Jun 20 2014 David Scott <dave.scott@citrix.com> - 0.9.7-2
- Update file list

* Fri Jun 20 2014 Bob Ball <bob.ball@citrix.com> - 0.9.7-1
- Update to 0.9.7: Rebase to xapi-project/sm b890746ea3b64058654947a6b74caf578cc11311

* Wed Apr 30 2014 Bob Ball <bob.ball@citrix.com> - 0.9.6-3
- Added fix for paths to blktap to use buildroot versions

* Tue Dec 10 2013 Euan Harris <euan.harris@eu.citrix.com> - 0.9.6-2
- Add dependency on xen-runtime

* Fri Nov 8 2013 Euan Harris <euan.harris@eu.citrix.com> - 0.9.6-1
- Update to 0.9.6, with fixes for iSCSI volumes on Ubuntu

* Mon Oct 28 2013 Euan Harris <euan.harris@eu.citrix.com>
- Update to 0.9.5, adding udev scripts and package dependencies needed to use iSCSI volumes

* Thu Oct 24 2013 Euan Harris <euan.harris@eu.citrix.com>
- Update to 0.9.4

* Wed Oct 23 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.3

* Wed Sep 11 2013 Euan Harris <euan.harris@citrix.com>
- Move drivers to _libdir/xapi/sm

* Mon Sep 09 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

