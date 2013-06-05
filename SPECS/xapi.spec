# -*- rpm-spec -*-

Summary: xapi - xen toolstack for XCP
Name:    xapi
Version: 1.9.0
Release: 0
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: xen-api-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires: pam-devel tetex-latex ocaml xen-devel zlib-devel
BuildRequires: ocaml-xcp-devel ocaml-xen-api-libs-transitional-devel
BuildRequires: ocaml-xen-api-client-devel omake ocaml-netdev-devel
BuildRequires: ocaml-cdrom-devel ocaml-fd-send-recv-devel forkexec-devel
BuildRequires: ocaml-libvhd-devel ocaml-nbd-devel ocaml-oclock-devel
BuildRequires: ocaml-ounit-devel ocaml-rpc-devel ocaml-ssl-devel ocaml-stdext-devel
BuildRequires: ocaml-syslog-devel ocaml-tapctl-devel ocaml-xen-lowlevel-libs-devel
BuildRequires: ocaml-xenstore-devel

%description
XCP toolstack.

%package core
Summary: The xapi toolstack
Group: System/Hypervisor

%description core
This package contains the xapi toolstack.

%package xe
Summary: The xapi toolstack CLI
Group: System/Hypervisor

%description xe
The command-line interface for controlling XCP hosts.

%package tests
Summary: Toolstack test programs
Group: System/Hypervisor

%description tests
This package contains a series of simple regression tests.

%package v6d
Summary: The editions and features daemon
Group: System/Hypervisor

%description v6d
This package contains daemon that defines and controls XCP editions and
associated features

%package rrdd
Summary: The RRD daemon
Group: System/Hypervisor

%description rrdd
This package contains a daemon that continually collects performance metrics
from the host and its VMs, stores the data in host's memory, and occasionally
synchronises the data to host's local storage.

%package xenops
Summary: Low-level debugging tools
Group: System/Hypervisor

%description xenops
This package contains the xenops-based low-level debugging tools.

%package client-devel
Summary: xapi Development Headers and Libraries
Group:   Development/Libraries

%description client-devel
This package contains the xapi development libraries and header files
for building addon tools.

%package datamodel-devel
Summary: xapi Datamodel headers and libraries
Group:   Development/Libraries

%description datamodel-devel
This package contains the internal xapi datamodel as a library suitable
for writing additional code generators.

%package rrd-devel
Summary: rrd-client headers and libraries
Group:   Development/Libraries

%description rrd-devel
This package contains rrd functions as a library suitable for writing tools 
related to rrd. Needed for rrd2csv and rrdd-plugins.

%prep 
%setup -q 
#%patch0 -p0 -b xapi-version.patch

%build
COMPILE_JAVA=no %{__make}

%install
rm -rf %{buildroot}

DESTDIR=$RPM_BUILD_ROOT %{__make} install

SITEDIR=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
for f in XenAPI XenAPIPlugin inventory; do
	for e in py pyc pyo; do
		echo $SITEDIR/$f.$e
	done
done > core-files

for e in py pyc pyo; do
	echo $SITEDIR/rrdd.$e
done > rrdd-files

ln -s /var/lib/xcp $RPM_BUILD_ROOT/var/xapi

%clean
rm -rf $RPM_BUILD_ROOT

%post core
[ ! -x /sbin/chkconfig ] || chkconfig --add xapi
[ ! -x /sbin/chkconfig ] || chkconfig --add xenservices
[ ! -x /sbin/chkconfig ] || chkconfig --add xapi-domains
[ ! -x /sbin/chkconfig ] || chkconfig --add perfmon
[ ! -x /sbin/chkconfig ] || chkconfig --add genptoken

%post v6d
[ ! -x /sbin/chkconfig ] || chkconfig --add v6d

%files core -f core-files
%defattr(-,root,root,-)
%{_bindir}/xapi
%config(noreplace) /etc/xapi.conf
/etc/logrotate.d/audit
/etc/logrotate.d/v6d
/etc/logrotate.d/xapi
/etc/pam.d/xapi
/etc/rc.d/init.d/management-interface
/etc/rc.d/init.d/perfmon
/etc/rc.d/init.d/xapi
/etc/rc.d/init.d/xapi-domains
%{_libexecdir}/xapi/xapissl
/etc/rc.d/init.d/xenservices
/etc/rc.d/init.d/genptoken
%config(noreplace) /etc/sysconfig/perfmon
%config(noreplace) /etc/sysconfig/xapi
/etc/xapi.d/base-path
/etc/xapi.d/plugins/*
%config(noreplace) /etc/xensource/db.conf
%config(noreplace) /etc/xensource/db.conf.rio
/etc/xensource/master.d/01-example
/etc/xensource/master.d/03-mpathalert-daemon
%config(noreplace) /etc/xensource/pool.conf
%{_bindir}/fix_firewall.sh
%{_bindir}/list_domains
%{_bindir}/mpathalert
%{_bindir}/perfmon
%{_bindir}/static-vdis
%{_bindir}/xapi-autostart-vms
%{_bindir}/xapi-db-process
%{_bindir}/xapi-wait-init-complete
%{_bindir}/xe-backup-metadata
%{_bindir}/xe-edit-bootloader
%{_bindir}/xe-get-network-backend
%{_bindir}/xe-mount-iso-sr
%{_bindir}/xe-restore-metadata
%{_bindir}/xe-reset-networking
%{_bindir}/xe-scsi-dev-map
%{_bindir}/xe-set-iscsi-iqn
%{_bindir}/xe-toolstack-restart
%{_bindir}/xe-xentrace
%{_bindir}/xe-switch-network-backend
/etc/bash_completion.d/xe-switch-network-backend
%{_bindir}/xsh
/etc/xensource/bugtool/xapi.xml
/etc/xensource/bugtool/xapi/stuff.xml
%{_libexecdir}/xapi/*
%config(noreplace) /etc/sparse_dd.conf
/var/lib/xcp/udhcpd.skel
/etc/xapi.d/host-post-declare-dead/10resetvdis
/var/xapi

%files xe
%defattr(-,root,root,-)
%{_bindir}/xe
/etc/bash_completion.d/xe

%files v6d
%defattr(-,root,root,-)
%{_sbindir}/v6d
/etc/rc.d/init.d/v6d

%files rrdd
%defattr(-,root,root,-)
%{_sbindir}/xcp-rrdd
/etc/rc.d/init.d/xcp-rrdd

%files xenops
%defattr(-,root,root,-)
%{_bindir}/xenops
%{_bindir}/add_vbd
%{_bindir}/add_vif
%{_bindir}/build_domain
%{_bindir}/build_hvm
%{_bindir}/create_domain
%{_bindir}/debug_ha_query_liveset
%{_bindir}/destroy_domain
%{_bindir}/event_listen
%{_bindir}/graph
%{_bindir}/memory_breakdown
%{_bindir}/memory_summary
%{_bindir}/pause_domain
%{_bindir}/restore_domain
%{_bindir}/shutdown_domain
%{_bindir}/sm_stress
%{_bindir}/suspend_domain
%{_bindir}/unpause_domain
%{_bindir}/vncproxy
%{_bindir}/with-vdi

%files tests
%defattr(-,root,root,-)
/etc/xapi.d/plugins/lvhdrt-helper
/etc/xapi.d/plugins/lvhdrt-trash-vdi
/etc/xapi.d/plugins/multipathrt-helper
%{_bindir}/cli-rt-domu-shar.sh
%{_bindir}/cli_test
%{_bindir}/install-debian-pv-inside.sh
%{_bindir}/install-debian-pv.sh
%{_bindir}/lvhdrt
%{_bindir}/multipathrt
%{_bindir}/myfirstpatch.asc
%{_bindir}/perftest
%{_bindir}/quicktest
%{_bindir}/quicktestbin
/cli-rt/*

%changelog








