# -*- rpm-spec -*-

Summary: sm - XCP storage managers
Name:    xcp-sm
Version: 0.9.0
Release: 1
Group:   System/Hypervisor
License: LGPL
URL:  http://www.citrix.com
Source0: https://github.com/euanh/sm/archive/%{version}/sm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: swig python-devel xen-devel

%description
This package contains storage backends used in XCP

%prep
%setup -q -n sm-%{version}

%build
DESTDIR=$RPM_BUILD_ROOT make

%install
make PLUGIN_SCRIPT_DEST=/usr/lib/xapi/plugins/ DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /sbin/chkconfig ] || chkconfig --add mpathroot

%files
%defattr(-,root,root,-)
/etc/cron.d/*
/etc/rc.d/init.d/snapwatchd
/etc/rc.d/init.d/mpathroot
/usr/lib/xapi/plugins/coalesce-leaf
/usr/lib/xapi/plugins/lvhd-thin
/usr/lib/xapi/plugins/nfs-on-slave
/usr/lib/xapi/plugins/on-slave
/usr/lib/xapi/plugins/tapdisk-pause
/usr/lib/xapi/plugins/testing-hooks
/usr/lib/xapi/plugins/vss_control
/usr/lib/xapi/plugins/intellicache-clean
/etc/xensource/master.d/02-vhdcleanup
/opt/xensource/bin/blktap2
/opt/xensource/bin/tapdisk-cache-stats
/opt/xensource/debug/tp
/opt/xensource/libexec/check-device-sharing
/opt/xensource/libexec/dcopy
/opt/xensource/libexec/local-device-change
/opt/xensource/sm/DummySR
/opt/xensource/sm/DummySR.py
/opt/xensource/sm/DummySR.pyc
/opt/xensource/sm/DummySR.pyo
/opt/xensource/sm/EXTSR
/opt/xensource/sm/EXTSR.py
/opt/xensource/sm/EXTSR.pyc
/opt/xensource/sm/EXTSR.pyo
/opt/xensource/sm/FileSR
/opt/xensource/sm/FileSR.py
/opt/xensource/sm/FileSR.pyc
/opt/xensource/sm/FileSR.pyo
/opt/xensource/sm/HBASR
/opt/xensource/sm/HBASR.py
/opt/xensource/sm/HBASR.pyc
/opt/xensource/sm/HBASR.pyo
/opt/xensource/sm/ISCSISR
/opt/xensource/sm/ISCSISR.py
/opt/xensource/sm/ISCSISR.pyc
/opt/xensource/sm/ISCSISR.pyo
/opt/xensource/sm/ISOSR
/opt/xensource/sm/ISOSR.py
/opt/xensource/sm/ISOSR.pyc
/opt/xensource/sm/ISOSR.pyo
/opt/xensource/sm/OCFSSR.py
/opt/xensource/sm/OCFSSR.pyc
/opt/xensource/sm/OCFSSR.pyo
/opt/xensource/sm/OCFSoISCSISR
/opt/xensource/sm/OCFSoISCSISR.py
/opt/xensource/sm/OCFSoISCSISR.pyc
/opt/xensource/sm/OCFSoISCSISR.pyo
/opt/xensource/sm/OCFSoHBASR
/opt/xensource/sm/OCFSoHBASR.py
/opt/xensource/sm/OCFSoHBASR.pyc
/opt/xensource/sm/OCFSoHBASR.pyo
/opt/xensource/sm/LUNperVDI.py
/opt/xensource/sm/LUNperVDI.pyc
/opt/xensource/sm/LUNperVDI.pyo
/opt/xensource/sm/LVHDSR.py
/opt/xensource/sm/LVHDSR.pyc
/opt/xensource/sm/LVHDSR.pyo
/opt/xensource/sm/LVHDoHBASR.py
/opt/xensource/sm/LVHDoHBASR.pyc
/opt/xensource/sm/LVHDoHBASR.pyo
/opt/xensource/sm/LVHDoISCSISR.py
/opt/xensource/sm/LVHDoISCSISR.pyc
/opt/xensource/sm/LVHDoISCSISR.pyo
/opt/xensource/sm/LVMSR
/opt/xensource/sm/LVMoHBASR
/opt/xensource/sm/LVMoISCSISR
/opt/xensource/sm/NFSSR
/opt/xensource/sm/NFSSR.py
/opt/xensource/sm/NFSSR.pyc
/opt/xensource/sm/NFSSR.pyo
/opt/xensource/sm/SHMSR.py
/opt/xensource/sm/SHMSR.pyc
/opt/xensource/sm/SHMSR.pyo
/opt/xensource/sm/SR.py
/opt/xensource/sm/SR.pyc
/opt/xensource/sm/SR.pyo
/opt/xensource/sm/SRCommand.py
/opt/xensource/sm/SRCommand.pyc
/opt/xensource/sm/SRCommand.pyo
/opt/xensource/sm/VDI.py
/opt/xensource/sm/VDI.pyc
/opt/xensource/sm/VDI.pyo
/opt/xensource/sm/XE_SR_ERRORCODES.xml
/opt/xensource/sm/blktap2.py
/opt/xensource/sm/blktap2.pyc
/opt/xensource/sm/blktap2.pyo
/opt/xensource/sm/cleanup.py
/opt/xensource/sm/cleanup.pyc
/opt/xensource/sm/cleanup.pyo
/opt/xensource/sm/devscan.py
/opt/xensource/sm/devscan.pyc
/opt/xensource/sm/devscan.pyo
/opt/xensource/sm/fjournaler.py
/opt/xensource/sm/fjournaler.pyc
/opt/xensource/sm/fjournaler.pyo
/opt/xensource/sm/flock.py
/opt/xensource/sm/flock.pyc
/opt/xensource/sm/flock.pyo
/opt/xensource/sm/ipc.py
/opt/xensource/sm/ipc.pyc
/opt/xensource/sm/ipc.pyo
/opt/xensource/sm/iscsilib.py
/opt/xensource/sm/iscsilib.pyc
/opt/xensource/sm/iscsilib.pyo
/opt/xensource/sm/journaler.py
/opt/xensource/sm/journaler.pyc
/opt/xensource/sm/journaler.pyo
/opt/xensource/sm/lcache.py
/opt/xensource/sm/lcache.pyc
/opt/xensource/sm/lcache.pyo
/opt/xensource/sm/lock.py
/opt/xensource/sm/lock.pyc
/opt/xensource/sm/lock.pyo
/opt/xensource/sm/lvhdutil.py
/opt/xensource/sm/lvhdutil.pyc
/opt/xensource/sm/lvhdutil.pyo
/opt/xensource/sm/lvmanager.py
/opt/xensource/sm/lvmanager.pyc
/opt/xensource/sm/lvmanager.pyo
/opt/xensource/sm/lvmcache.py
/opt/xensource/sm/lvmcache.pyc
/opt/xensource/sm/lvmcache.pyo
/opt/xensource/sm/lvutil.py
/opt/xensource/sm/lvutil.pyc
/opt/xensource/sm/lvutil.pyo
/opt/xensource/sm/metadata.py
/opt/xensource/sm/metadata.pyc
/opt/xensource/sm/metadata.pyo
/opt/xensource/sm/srmetadata.py
/opt/xensource/sm/srmetadata.pyc
/opt/xensource/sm/srmetadata.pyo
/opt/xensource/sm/mpath_cli.py
/opt/xensource/sm/mpath_cli.pyc
/opt/xensource/sm/mpath_cli.pyo
/opt/xensource/sm/mpath_dmp.py
/opt/xensource/sm/mpath_dmp.pyc
/opt/xensource/sm/mpath_dmp.pyo
/opt/xensource/sm/mpath_null.py
/opt/xensource/sm/mpath_null.pyc
/opt/xensource/sm/mpath_null.pyo
/opt/xensource/sm/mpathcount.py
/opt/xensource/sm/mpathcount.pyc
/opt/xensource/sm/mpathcount.pyo
/opt/xensource/sm/mpathutil.py
/opt/xensource/sm/mpathutil.pyc
/opt/xensource/sm/mpathutil.pyo
/opt/xensource/sm/mpp_luncheck.py
/opt/xensource/sm/mpp_luncheck.pyc
/opt/xensource/sm/mpp_luncheck.pyo
/opt/xensource/sm/mpp_mpathutil.py
/opt/xensource/sm/mpp_mpathutil.pyc
/opt/xensource/sm/mpp_mpathutil.pyo
/opt/xensource/sm/nfs.py
/opt/xensource/sm/nfs.pyc
/opt/xensource/sm/nfs.pyo
/opt/xensource/sm/refcounter.py
/opt/xensource/sm/refcounter.pyc
/opt/xensource/sm/refcounter.pyo
/opt/xensource/sm/resetvdis.py
/opt/xensource/sm/resetvdis.pyc
/opt/xensource/sm/resetvdis.pyo
/opt/xensource/sm/scsiutil.py
/opt/xensource/sm/scsiutil.pyc
/opt/xensource/sm/scsiutil.pyo
/opt/xensource/sm/scsi_host_rescan.py
/opt/xensource/sm/scsi_host_rescan.pyc
/opt/xensource/sm/scsi_host_rescan.pyo
/opt/xensource/sm/snapwatchd/_xslib.so
/opt/xensource/sm/snapwatchd/snapwatchd
/opt/xensource/sm/snapwatchd/xslib.py
/opt/xensource/sm/snapwatchd/xslib.pyc
/opt/xensource/sm/snapwatchd/xslib.pyo
/opt/xensource/sm/sysdevice.py
/opt/xensource/sm/sysdevice.pyc
/opt/xensource/sm/sysdevice.pyo
/opt/xensource/sm/udevSR
/opt/xensource/sm/udevSR.py
/opt/xensource/sm/udevSR.pyc
/opt/xensource/sm/udevSR.pyo
/opt/xensource/sm/updatempppathd.py
/opt/xensource/sm/updatempppathd.pyc
/opt/xensource/sm/updatempppathd.pyo
/opt/xensource/sm/util.py
/opt/xensource/sm/util.pyc
/opt/xensource/sm/util.pyo
/opt/xensource/sm/verifyVHDsOnSR.py
/opt/xensource/sm/verifyVHDsOnSR.pyc
/opt/xensource/sm/verifyVHDsOnSR.pyo
/opt/xensource/sm/vhdutil.py
/opt/xensource/sm/vhdutil.pyc
/opt/xensource/sm/vhdutil.pyo
/opt/xensource/sm/vss_control
/opt/xensource/sm/xs_errors.py
/opt/xensource/sm/xs_errors.pyc
/opt/xensource/sm/xs_errors.pyo
/sbin/mpathutil


%package rawhba
Group:   System/Hypervisor
Summary: rawhba SR type capability
#Requires: sm = @SM_VERSION@-@SM_RELEASE@

%description rawhba
This package adds a new rawhba SR type. This SR type allows utilization of
Fiber Channel raw LUNs as separate VDIs (LUN per VDI)

%files rawhba
/opt/xensource/sm/RawHBASR
/opt/xensource/sm/RawHBASR.py
/opt/xensource/sm/RawHBASR.pyc
/opt/xensource/sm/RawHBASR.pyo
/opt/xensource/sm/B_util.py
/opt/xensource/sm/B_util.pyc
/opt/xensource/sm/B_util.pyo

%changelog

* Mon Sep 09 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

