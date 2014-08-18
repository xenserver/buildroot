# -*- rpm-spec -*-

Summary: XCP storage managers
Name:    xcp-sm
Version: 0.9.7
Release: 4%{?dist}
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
make PLUGIN_SCRIPT_DEST=/usr/lib/xapi/plugins/ SM_DEST=/usr/lib/xapi/sm/ BLKTAP_ROOT=%{_libdir}/blktap INVENTORY=/etc/xcp/inventory DESTDIR=$RPM_BUILD_ROOT install
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 xcp-mpath-scsidev-rules %{buildroot}/etc/udev/rules.d/55-xs-mpath-scsidev.rules
mkdir -p %{buildroot}/etc/udev/scripts
install -m 0755 xcp-mpath-scsidev-script %{buildroot}/etc/udev/scripts/xs-mpath-scsidev.sh


%post
[ ! -x /sbin/chkconfig ] || chkconfig --add mpathroot

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
/etc/udev/rules.d/55-xs-mpath-scsidev.rules
/etc/udev/scripts/xs-mpath-scsidev.sh
/usr/lib/xapi/plugins/coalesce-leaf
/usr/lib/xapi/plugins/lvhd-thin
/usr/lib/xapi/plugins/nfs-on-slave
/usr/lib/xapi/plugins/on-slave
/usr/lib/xapi/plugins/tapdisk-pause
/usr/lib/xapi/plugins/testing-hooks
/usr/lib/xapi/plugins/vss_control
/usr/lib/xapi/plugins/intellicache-clean
/usr/lib/xapi/plugins/trim
/etc/xensource/master.d/02-vhdcleanup
/opt/xensource/bin/blktap2
/opt/xensource/bin/tapdisk-cache-stats
/opt/xensource/debug/tp
/opt/xensource/libexec/check-device-sharing
/opt/xensource/libexec/dcopy
/opt/xensource/libexec/local-device-change
/usr/lib/xapi/sm/DummySR
/usr/lib/xapi/sm/DummySR.py
/usr/lib/xapi/sm/DummySR.pyc
/usr/lib/xapi/sm/DummySR.pyo
/usr/lib/xapi/sm/EXTSR
/usr/lib/xapi/sm/EXTSR.py
/usr/lib/xapi/sm/EXTSR.pyc
/usr/lib/xapi/sm/EXTSR.pyo
/usr/lib/xapi/sm/FileSR
/usr/lib/xapi/sm/FileSR.py
/usr/lib/xapi/sm/FileSR.pyc
/usr/lib/xapi/sm/FileSR.pyo
/usr/lib/xapi/sm/HBASR
/usr/lib/xapi/sm/HBASR.py
/usr/lib/xapi/sm/HBASR.pyc
/usr/lib/xapi/sm/HBASR.pyo
/usr/lib/xapi/sm/ISCSISR
/usr/lib/xapi/sm/ISCSISR.py
/usr/lib/xapi/sm/ISCSISR.pyc
/usr/lib/xapi/sm/ISCSISR.pyo
/usr/lib/xapi/sm/ISOSR
/usr/lib/xapi/sm/ISOSR.py
/usr/lib/xapi/sm/ISOSR.pyc
/usr/lib/xapi/sm/ISOSR.pyo
/usr/lib/xapi/sm/LUNperVDI.py
/usr/lib/xapi/sm/LUNperVDI.pyc
/usr/lib/xapi/sm/LUNperVDI.pyo
/usr/lib/xapi/sm/LVHDSR.py
/usr/lib/xapi/sm/LVHDSR.pyc
/usr/lib/xapi/sm/LVHDSR.pyo
/usr/lib/xapi/sm/LVHDoHBASR.py
/usr/lib/xapi/sm/LVHDoHBASR.pyc
/usr/lib/xapi/sm/LVHDoHBASR.pyo
/usr/lib/xapi/sm/LVHDoISCSISR.py
/usr/lib/xapi/sm/LVHDoISCSISR.pyc
/usr/lib/xapi/sm/LVHDoISCSISR.pyo
/usr/lib/xapi/sm/LVMSR
/usr/lib/xapi/sm/LVMoHBASR
/usr/lib/xapi/sm/LVMoISCSISR
/usr/lib/xapi/sm/NFSSR
/usr/lib/xapi/sm/NFSSR.py
/usr/lib/xapi/sm/NFSSR.pyc
/usr/lib/xapi/sm/NFSSR.pyo
/usr/lib/xapi/sm/SHMSR.py
/usr/lib/xapi/sm/SHMSR.pyc
/usr/lib/xapi/sm/SHMSR.pyo
/usr/lib/xapi/sm/SR.py
/usr/lib/xapi/sm/SR.pyc
/usr/lib/xapi/sm/SR.pyo
/usr/lib/xapi/sm/SRCommand.py
/usr/lib/xapi/sm/SRCommand.pyc
/usr/lib/xapi/sm/SRCommand.pyo
/usr/lib/xapi/sm/VDI.py
/usr/lib/xapi/sm/VDI.pyc
/usr/lib/xapi/sm/VDI.pyo
/usr/lib/xapi/sm/XE_SR_ERRORCODES.xml
/usr/lib/xapi/sm/blktap2.py
/usr/lib/xapi/sm/blktap2.pyc
/usr/lib/xapi/sm/blktap2.pyo
/usr/lib/xapi/sm/constants.py
/usr/lib/xapi/sm/constants.pyc
/usr/lib/xapi/sm/constants.pyo
/usr/lib/xapi/sm/cleanup.py
/usr/lib/xapi/sm/cleanup.pyc
/usr/lib/xapi/sm/cleanup.pyo
/usr/lib/xapi/sm/devscan.py
/usr/lib/xapi/sm/devscan.pyc
/usr/lib/xapi/sm/devscan.pyo
/usr/lib/xapi/sm/fjournaler.py
/usr/lib/xapi/sm/fjournaler.pyc
/usr/lib/xapi/sm/fjournaler.pyo
/usr/lib/xapi/sm/flock.py
/usr/lib/xapi/sm/flock.pyc
/usr/lib/xapi/sm/flock.pyo
/usr/lib/xapi/sm/ipc.py
/usr/lib/xapi/sm/ipc.pyc
/usr/lib/xapi/sm/ipc.pyo
/usr/lib/xapi/sm/iscsilib.py
/usr/lib/xapi/sm/iscsilib.pyc
/usr/lib/xapi/sm/iscsilib.pyo
/usr/lib/xapi/sm/journaler.py
/usr/lib/xapi/sm/journaler.pyc
/usr/lib/xapi/sm/journaler.pyo
/usr/lib/xapi/sm/lcache.py
/usr/lib/xapi/sm/lcache.pyc
/usr/lib/xapi/sm/lcache.pyo
/usr/lib/xapi/sm/lock.py
/usr/lib/xapi/sm/lock.pyc
/usr/lib/xapi/sm/lock.pyo
/usr/lib/xapi/sm/lvhdutil.py
/usr/lib/xapi/sm/lvhdutil.pyc
/usr/lib/xapi/sm/lvhdutil.pyo
/usr/lib/xapi/sm/lvmanager.py
/usr/lib/xapi/sm/lvmanager.pyc
/usr/lib/xapi/sm/lvmanager.pyo
/usr/lib/xapi/sm/lvmcache.py
/usr/lib/xapi/sm/lvmcache.pyc
/usr/lib/xapi/sm/lvmcache.pyo
/usr/lib/xapi/sm/lvutil.py
/usr/lib/xapi/sm/lvutil.pyc
/usr/lib/xapi/sm/lvutil.pyo
/usr/lib/xapi/sm/metadata.py
/usr/lib/xapi/sm/metadata.pyc
/usr/lib/xapi/sm/metadata.pyo
/usr/lib/xapi/sm/srmetadata.py
/usr/lib/xapi/sm/srmetadata.pyc
/usr/lib/xapi/sm/srmetadata.pyo
/usr/lib/xapi/sm/mpath_cli.py
/usr/lib/xapi/sm/mpath_cli.pyc
/usr/lib/xapi/sm/mpath_cli.pyo
/usr/lib/xapi/sm/mpath_dmp.py
/usr/lib/xapi/sm/mpath_dmp.pyc
/usr/lib/xapi/sm/mpath_dmp.pyo
/usr/lib/xapi/sm/mpath_null.py
/usr/lib/xapi/sm/mpath_null.pyc
/usr/lib/xapi/sm/mpath_null.pyo
/usr/lib/xapi/sm/mpathcount.py
/usr/lib/xapi/sm/mpathcount.pyc
/usr/lib/xapi/sm/mpathcount.pyo
/usr/lib/xapi/sm/mpathutil.py
/usr/lib/xapi/sm/mpathutil.pyc
/usr/lib/xapi/sm/mpathutil.pyo
/usr/lib/xapi/sm/mpp_luncheck.py
/usr/lib/xapi/sm/mpp_luncheck.pyc
/usr/lib/xapi/sm/mpp_luncheck.pyo
/usr/lib/xapi/sm/mpp_mpathutil.py
/usr/lib/xapi/sm/mpp_mpathutil.pyc
/usr/lib/xapi/sm/mpp_mpathutil.pyo
/usr/lib/xapi/sm/nfs.py
/usr/lib/xapi/sm/nfs.pyc
/usr/lib/xapi/sm/nfs.pyo
/usr/lib/xapi/sm/refcounter.py
/usr/lib/xapi/sm/refcounter.pyc
/usr/lib/xapi/sm/refcounter.pyo
/usr/lib/xapi/sm/resetvdis.py
/usr/lib/xapi/sm/resetvdis.pyc
/usr/lib/xapi/sm/resetvdis.pyo
/usr/lib/xapi/sm/scsiutil.py
/usr/lib/xapi/sm/scsiutil.pyc
/usr/lib/xapi/sm/scsiutil.pyo
/usr/lib/xapi/sm/scsi_host_rescan.py
/usr/lib/xapi/sm/scsi_host_rescan.pyc
/usr/lib/xapi/sm/scsi_host_rescan.pyo
/usr/lib/xapi/sm/snapwatchd/snapwatchd
/usr/lib/xapi/sm/snapwatchd/xslib.py
/usr/lib/xapi/sm/snapwatchd/xslib.pyc
/usr/lib/xapi/sm/snapwatchd/xslib.pyo
/usr/lib/xapi/sm/snapwatchd/snapdebug.py
/usr/lib/xapi/sm/snapwatchd/snapdebug.pyc
/usr/lib/xapi/sm/snapwatchd/snapdebug.pyo
/usr/lib/xapi/sm/sysdevice.py
/usr/lib/xapi/sm/sysdevice.pyc
/usr/lib/xapi/sm/sysdevice.pyo
/usr/lib/xapi/sm/udevSR
/usr/lib/xapi/sm/udevSR.py
/usr/lib/xapi/sm/udevSR.pyc
/usr/lib/xapi/sm/udevSR.pyo
/usr/lib/xapi/sm/updatempppathd.py
/usr/lib/xapi/sm/updatempppathd.pyc
/usr/lib/xapi/sm/updatempppathd.pyo
/usr/lib/xapi/sm/util.py
/usr/lib/xapi/sm/util.pyc
/usr/lib/xapi/sm/util.pyo
/usr/lib/xapi/sm/verifyVHDsOnSR.py
/usr/lib/xapi/sm/verifyVHDsOnSR.pyc
/usr/lib/xapi/sm/verifyVHDsOnSR.pyo
/usr/lib/xapi/sm/vhdutil.py
/usr/lib/xapi/sm/vhdutil.pyc
/usr/lib/xapi/sm/vhdutil.pyo
/usr/lib/xapi/sm/trim_util.py
/usr/lib/xapi/sm/trim_util.pyc
/usr/lib/xapi/sm/trim_util.pyo
/usr/lib/xapi/sm/vss_control
/usr/lib/xapi/sm/xs_errors.py
/usr/lib/xapi/sm/xs_errors.pyc
/usr/lib/xapi/sm/xs_errors.pyo
/sbin/mpathutil
%config /etc/multipath.xenserver/multipath.conf


%package rawhba
Summary: XCP rawhba SR type capability
#Requires: sm = @SM_VERSION@-@SM_RELEASE@

%description rawhba
This package adds a new rawhba SR type. This SR type allows utilization of
Fiber Channel raw LUNs as separate VDIs (LUN per VDI)

%files rawhba
%exclude /usr/lib/xapi/sm/RawHBASR
/usr/lib/xapi/sm/RawHBASR.py
/usr/lib/xapi/sm/RawHBASR.pyc
/usr/lib/xapi/sm/RawHBASR.pyo
/usr/lib/xapi/sm/B_util.py
/usr/lib/xapi/sm/B_util.pyc
/usr/lib/xapi/sm/B_util.pyo
/usr/lib/xapi/sm/enable-borehamwood

%changelog
* Tue Sep 30 2014 Bob Ball <bob.ball@citrix.com> - 0.9.7-4
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
- Move drivers to /usr/lib/xapi/sm

* Mon Sep 09 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

