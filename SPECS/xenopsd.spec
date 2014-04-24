Name:           xenopsd
Version:        0.9.34
Release:        1%{?dist}
Summary:        Simple VM manager
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xenopsd
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xenopsd-xc-init
Source2:        xenopsd-simulator-init
Source3:        xenopsd-libvirt-init
Source4:        xenopsd-xenlight-init
Source5:        make-xsc-xenopsd.conf
Source6:        xenopsd-network-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  libvirt-devel
BuildRequires:  ocaml-libvirt-devel
BuildRequires:  ocaml-qmp-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  message-switch-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  xen-devel
BuildRequires:  linux-guest-loader
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  vncterm
BuildRequires:  ocaml-uutf-devel
Requires:       message-switch
Requires:       redhat-lsb-core
Requires:       xenops-cli

%description
Simple VM manager for the xapi toolstack.

%package        libvirt
Summary:        Xenopsd using libvirt
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       libvirt

%description    libvirt
Simple VM manager for Xen and KVM using libvirt.


%package        xc
Summary:        Xenopsd using xc
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd
Requires:       vncterm
Requires:       xen-libs

%description    xc
Simple VM manager for Xen using libxc.

%package        simulator
Summary:        Xenopsd simulator
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    simulator
A synthetic VM manager for testing.

#%package        xenlight
#Summary:        Xenopsd using libxenlight
#Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}
#%description    xenlight
#Simple VM manager for Xen using libxenlight

%prep
%setup -q
cp %{SOURCE1} xenopsd-xc-init
cp %{SOURCE2} xenopsd-simulator-init
cp %{SOURCE3} xenopsd-libvirt-init
cp %{SOURCE4} xenopsd-xenlight-init
cp %{SOURCE5} make-xsc-xenopsd.conf
cp %{SOURCE6} xenopsd-network-conf

%build
make configure
./configure --libexecdir %{_libexecdir}/%{name}
make

%install
mkdir -p %{buildroot}/%{_sbindir}

install -D _build/libvirt/xenops_libvirt_main.native     %{buildroot}/%{_sbindir}/xenopsd-libvirt
install -D _build/simulator/xenops_simulator_main.native %{buildroot}/%{_sbindir}/xenopsd-simulator
install -D _build/xc/xenops_xc_main.native               %{buildroot}/%{_sbindir}/xenopsd-xc
#install -D _build/xl/xenops_xl_main.native               %{buildroot}/%{_sbindir}/xenopsd-xenlight
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
install -D _build/xenguest/xenguest_main.native          %{buildroot}/%{_libexecdir}/%{name}/xenguest
install -D scripts/vif %{buildroot}/%{_libexecdir}/%{name}/vif
install -D scripts/vif-real %{buildroot}/%{_libexecdir}/%{name}/vif-real
install -D scripts/vif-xl %{buildroot}/%{_libexecdir}/%{name}/vif-xl
install -D scripts/qemu-dm-wrapper %{buildroot}/%{_libexecdir}/%{name}/qemu-dm-wrapper
install -D scripts/qemu-vif-script %{buildroot}/%{_libexecdir}/%{name}/qemu-vif-script
install -D scripts/setup-vif-rules %{buildroot}/%{_libexecdir}/%{name}/setup-vif-rules
install -D scripts/common.py %{buildroot}/%{_libexecdir}/%{name}/common.py
install -D scripts/network.conf %{buildroot}/%{_libexecdir}/%{name}/network.conf

mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xenopsd-libvirt-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-libvirt
install -m 0755 xenopsd-xc-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-xc
install -m 0755 xenopsd-simulator-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-simulator
#install -m 0755 xenopsd-xenlight-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-xenlight

mkdir -p %{buildroot}/etc/xapi
chmod 755 make-xsc-xenopsd.conf 
LIBEXECDIR=%{_libexecdir}/%{name} ETCDIR=/etc/xapi SCRIPTSDIR=%{_libexecdir}/%{name} DESTDIR=%{buildroot} ./make-xsc-xenopsd.conf > xenopsd-conf
install -m 0644 xenopsd-conf %{buildroot}/etc/xenopsd.conf
install -m 0644 xenopsd-network-conf %{buildroot}/etc/xapi/network.conf


%files
%doc README.md LICENSE
%{_libexecdir}/%{name}/vif
%{_libexecdir}/%{name}/vif-real
%{_libexecdir}/%{name}/vif-xl
%{_libexecdir}/%{name}/qemu-dm-wrapper
%{_libexecdir}/%{name}/qemu-vif-script
%{_libexecdir}/%{name}/setup-vif-rules
%{_libexecdir}/%{name}/network.conf
%{_libexecdir}/%{name}/common.py
%{_libexecdir}/%{name}/common.pyo
%{_libexecdir}/%{name}/common.pyc
/etc/xenopsd.conf
/etc/xapi/network.conf

%files libvirt
%{_sbindir}/xenopsd-libvirt
%{_sysconfdir}/init.d/xenopsd-libvirt

%post libvirt
/sbin/chkconfig --add xenopsd-libvirt

%preun libvirt
if [ $1 -eq 0 ]; then
  /sbin/service xenopsd-libvirt stop > /dev/null 2>&1
  /sbin/chkconfig --del xenopsd-libvirt
fi

%files xc
%{_sbindir}/xenopsd-xc
%{_sysconfdir}/init.d/xenopsd-xc
%{_libexecdir}/%{name}/xenguest

%post xc
/sbin/chkconfig --add xenopsd-xc

%preun xc
if [ $1 -eq 0 ]; then
  /sbin/service xenopsd-xc stop > /dev/null 2>&1
  /sbin/chkconfig --del xenopsd-xc
fi

%files simulator
%{_sbindir}/xenopsd-simulator
%{_sysconfdir}/init.d/xenopsd-simulator

%post simulator
/sbin/chkconfig --add xenopsd-simulator

%preun simulator
if [ $1 -eq 0 ]; then
  /sbin/service xenopsd-simulator stop > /dev/null 2>&1
  /sbin/chkconfig --del xenopsd-simulator
fi

#%files xenlight
#%defattr(-,root,root)
#%{_sbindir}/xenopsd-xenlight
#%{_sysconfdir}/init.d/xenopsd-xenlight

#%post xenlight
#/sbin/chkconfig --add xenopsd-xenlight

#%preun xenlight
#if [ $1 -eq 0 ]; then
#  /sbin/service xenopsd-xenlight stop > /dev/null 2>&1
#  /sbin/chkconfig --del xenopsd-xenlight
#fi

%changelog
* Fri Jan 17 2014 Euan Harris <euan.harris@eu.citrix.com> - 0.9.34-1
- Update to 0.9.34, restoring fixes from the 0.9.32 line which were 
  not merged to trunk before 0.9.33 was tagged

* Wed Dec 4 2013 Euan Harris <euan.harris@eu.citrix.com> - 0.9.33-1
- Update to 0.9.33, with fixes for suspending and resuming HVM guests

* Mon Oct 28 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.32-1
- Update to 0.9.32, with udev fix (no more "task was asynchronously cancelled")

* Mon Oct 21 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.31
- move scripts back to libexecdir

* Sun Oct 20 2013 David Scott <dave.scott@eu.citrix.com>
- give up on making libxl work, since it requires xen-4.4
- move scripts from libexecdir to libdir

* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com>
- update to 0.9.29

* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com>
- update to 0.9.28

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- modprobe blk{tap,back} in the xenopsd-xc init.d script since
  we need these to make virtual disks work
- update to 0.9.27

* Tue Sep 24 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.26, which includes fixes for networking and libxl

* Fri Sep 20 2013 Euan Harris <euan.harris@citrix.com>
- Generate xenopsd.conf automatically

* Mon Sep 16 2013 Euan Harris <euan.harris@citrix.com>
- Update to 0.9.25, which includes linker paths required on Debian

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.24

* Fri Jun 21 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.5, which includes xenopsd-xenlight

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package
