Name:           xenopsd
Version:        0.9.1
Release:        2
Summary:        Simple VM manager
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xenopsd/archive/xenopsd-0.9.1.tar.gz
Source0:        xenopsd-0.9.1.tar.gz
Source1:        xenopsd-xc-init
Source2:        xenopsd-simulator-init
Source3:        xenopsd-libvirt-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-oclock-devel ocaml-uuidm-devel forkexec-devel
BuildRequires:  ocaml-libvirt-devel libvirt-devel ocaml-qmp-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel ocaml-sexplib
BuildRequires:  ocaml-xenstore-clients-devel ocaml-xenstore-devel
BuildRequires:  xen-devel
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
Requires:       xen-libs

%description    xc
Simple VM manager for Xen using libxc.

%package        simulator
Summary:        %{name} using libvirt
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    simulator
A synthetic VM manager for testing.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
./configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}

install -D dist/build/xenopsd_libvirt/xenopsd_libvirt %{buildroot}/%{_sbindir}/xenopsd-libvirt
install -D dist/build/xenopsd/xenopsd %{buildroot}/%{_sbindir}/xenopsd-xc
install -D dist/build/xenopsd_simulator/xenopsd_simulator %{buildroot}/%{_sbindir}/xenopsd-simulator
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
install -D dist/build/xenguest/xenguest %{buildroot}/%{_libexecdir}/%{name}/xenguest
install -D scripts/vif %{buildroot}/%{_libexecdir}/%{name}/vif
install -D scripts/qemu-dm-wrapper %{buildroot}/%{_libexecdir}/%{name}/qemu-dm-wrapper
install -D scripts/qemu-vif-script %{buildroot}/%{_libexecdir}/%{name}/qemu-vif-script
install -D scripts/setup-vif-rules %{buildroot}/%{_libexecdir}/%{name}/setup-vif-rules
install -D scripts/common.py %{buildroot}/%{_libexecdir}/%{name}/common.py
install -D scripts/network.conf %{buildroot}/%{_libexecdir}/%{name}/network.conf

mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/xenopsd-libvirt-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-libvirt
install -m 0755 %{_sourcedir}/xenopsd-xc-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-xc
install -m 0755 %{_sourcedir}/xenopsd-simulator-init %{buildroot}/%{_sysconfdir}/init.d/xenopsd-simulator

mkdir -p %{buildroot}/etc
DESTDIR=%{buildroot} ETCDIR=/etc SBINDIR=%{_sbindir} LIBEXECDIR=%{_libexecdir}/%{name} SCRIPTSDIR=%{_libexecdir}/%{name} scripts/make-custom-xenopsd.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_libexecdir}/%{name}/vif
%{_libexecdir}/%{name}/qemu-dm-wrapper
%{_libexecdir}/%{name}/qemu-vif-script
%{_libexecdir}/%{name}/setup-vif-rules
%{_libexecdir}/%{name}/network.conf
%{_libexecdir}/%{name}/common.py
%{_libexecdir}/%{name}/common.pyo
%{_libexecdir}/%{name}/common.pyc
/etc/xenopsd.conf

%files libvirt
%defattr(-,root,root)
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

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

