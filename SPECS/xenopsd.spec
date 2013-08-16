Name:           xenopsd
Version:        0.9.21
Release:        0
Summary:        Simple VM manager
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xenopsd/archive/%{version}.tar.gz
Source0:        https://github.com/djs55/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xenopsd-xc-init
Source2:        xenopsd-simulator-init
Source3:        xenopsd-libvirt-init
Source4:        xenopsd-xenlight-init
Source5:        xenopsd-conf
Source6:        xenopsd-network-conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-oclock-devel ocaml-uuidm-devel forkexecd-devel
BuildRequires:  ocaml-libvirt-devel libvirt-devel ocaml-qmp-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel ocaml-sexplib
BuildRequires:  ocaml-xenstore-clients-devel ocaml-xenstore-devel
BuildRequires:  xen-devel ocaml-xcp-inventory-devel
Requires:       message-switch xenops-cli

%description
Simple VM manager for the xapi toolstack.

%package        libvirt
Summary:        %{name} using libvirt
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       libvirt

%description    libvirt
Simple VM manager for Xen and KVM using libvirt.


%package        xc
Summary:        %{name} using xc
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       xen-libs vncterm forkexecd

%description    xc
Simple VM manager for Xen using libxc.

%package        simulator
Summary:        %{name} using libvirt
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    simulator
A synthetic VM manager for testing.

%package        xenlight
Summary:        %{name} using libxenlight
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    xenlight
Simple VM manager for Xen using libxenlight

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}

#install -D _build/libvirt/xenops_libvirt_main.native     %{buildroot}/%{_sbindir}/xenopsd-libvirt
install -D _build/simulator/xenops_simulator_main.native %{buildroot}/%{_sbindir}/xenopsd-simulator
install -D _build/xc/xenops_xc_main.native               %{buildroot}/%{_sbindir}/xenopsd-xc
install -D _build/xl/xenops_xl_main.native               %{buildroot}/%{_sbindir}/xenopsd-xenlight
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
install -D _build/xenguest/xenguest_main.native          %{buildroot}/%{_libexecdir}/%{name}/xenguest
install -D scripts/vif %{buildroot}/%{_libexecdir}/%{name}/vif
install -D scripts/vif-xl %{buildroot}/%{_libexecdir}/%{name}/vif-xl
install -D scripts/qemu-dm-wrapper %{buildroot}/%{_libexecdir}/%{name}/qemu-dm-wrapper
install -D scripts/qemu-vif-script %{buildroot}/%{_libexecdir}/%{name}/qemu-vif-script
install -D scripts/setup-vif-rules %{buildroot}/%{_libexecdir}/%{name}/setup-vif-rules
install -D scripts/common.py %{buildroot}/%{_libexecdir}/%{name}/common.py
install -D scripts/network.conf %{buildroot}/%{_libexecdir}/%{name}/network.conf

mkdir -p %{buildroot}%{_sysconfdir}/init.d
#install -m 0755 %{_sourcedir}/xenopsd-libvirt-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-libvirt
install -m 0755 %{_sourcedir}/xenopsd-xc-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-xc
install -m 0755 %{_sourcedir}/xenopsd-simulator-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-simulator
install -m 0755 %{_sourcedir}/xenopsd-xenlight-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-xenlight
mkdir -p %{buildroot}/etc/xapi
install -m 0644 %{_sourcedir}/xenopsd-conf %{buildroot}/etc/xenopsd.conf
install -m 0644 %{_sourcedir}/xenopsd-network-conf %{buildroot}/etc/xapi/network.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_libexecdir}/%{name}/vif
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
#%defattr(-,root,root)
#%{_sbindir}/xenopsd-libvirt
#%{_sysconfdir}/init.d/xenopsd-libvirt

%post libvirt
/sbin/chkconfig --add xenopsd-libvirt

%preun libvirt
if [ $1 -eq 0 ]; then
  /sbin/service xenopsd-libvirt stop > /dev/null 2>&1
  /sbin/chkconfig --del xenopsd-libvirt
fi

%files xc
%defattr(-,root,root)
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
%defattr(-,root,root)
%{_sbindir}/xenopsd-simulator
%{_sysconfdir}/init.d/xenopsd-simulator

%post simulator
/sbin/chkconfig --add xenopsd-simulator

%preun simulator
if [ $1 -eq 0 ]; then
  /sbin/service xenopsd-simulator stop > /dev/null 2>&1
  /sbin/chkconfig --del xenopsd-simulator
fi

%files xenlight
%defattr(-,root,root)
%{_sbindir}/xenopsd-xenlight
%{_sysconfdir}/init.d/xenopsd-xenlight

%post xenlight
/sbin/chkconfig --add xenopsd-xenlight

%preun xenlight
if [ $1 -eq 0 ]; then
  /sbin/service xenopsd-xenlight stop > /dev/null 2>&1
  /sbin/chkconfig --del xenopsd-xenlight
fi

%changelog
* Fri Jun 21 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.5, which includes xenopsd-xenlight

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package
