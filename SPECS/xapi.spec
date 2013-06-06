# -*- rpm-spec -*-

Summary: xapi - xen toolstack for XCP
Name:    xapi
Version: 1.9.2
Release: 0
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: xen-api-%{version}.tar.gz
Source1: xen-api-xapi-conf
Source2: xen-api-init
Source3: xen-api-xapissl
Source4: xen-api-xapissl-conf
Source5: xen-api-db-conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc
BuildRequires: pam-devel tetex-latex ocaml xen-devel zlib-devel
BuildRequires: ocaml-xcp-idl-devel ocaml-xen-api-libs-transitional-devel
BuildRequires: ocaml-xen-api-client-devel omake ocaml-netdev-devel
BuildRequires: ocaml-cdrom-devel ocaml-fd-send-recv-devel forkexec-devel
BuildRequires: ocaml-libvhd-devel ocaml-nbd-devel ocaml-oclock-devel
BuildRequires: ocaml-ounit-devel ocaml-rpc-devel ocaml-ssl-devel ocaml-stdext-devel
BuildRequires: ocaml-syslog-devel ocaml-tapctl-devel ocaml-xen-lowlevel-libs-devel
BuildRequires: ocaml-xenstore-devel git cmdliner-devel ocaml-xcp-inventory-devel
BuildRequires: ocaml-bitstring-devel libuuid-devel make utop
Requires: stunnel ocaml-xcp-inventory

%description
XCP toolstack.

%description
This package contains the xapi toolstack.

%package xe
Summary: The xapi toolstack CLI
Group: System/Hypervisor

%description xe
The command-line interface for controlling XCP hosts.

%prep 
%setup -q -n xen-api-%{version}
#%patch0 -p0 -b xapi-version.patch

%build
./configure --bindir=%{_bindir} --etcdir=/etc --libexecdir=%{_libexecdir}/xapi \
            --xapiconf=/etc/xapi.conf --hooksdir=/etc/xapi/hook-scripts

export COMPILE_JAVA=no
make version
omake phase1
omake phase2
omake ocaml/xapi/xapi
omake ocaml/xe-cli/xe

%install
rm -rf %{buildroot}
 
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 ocaml/xapi/xapi.opt %{buildroot}/%{_sbindir}/xapi
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/xen-api-init %{buildroot}%{_sysconfdir}/init.d/xapi
mkdir -p %{buildroot}/%{_libexecdir}/xapi
install -m 0755 %{_sourcedir}/xen-api-xapissl %{buildroot}/%{_libexecdir}/xapi/xapissl
install -m 0755 scripts/pci-info %{buildroot}/%{_libexecdir}/xapi/pci-info
mkdir -p %{buildroot}/etc/xapi
install -m 0644 %{_sourcedir}/xen-api-xapi-conf %{buildroot}/etc/xapi.conf
install -m 0644 %{_sourcedir}/xen-api-db-conf %{buildroot}/etc/xapi/db.conf
install -m 0644 %{_sourcedir}/xen-api-xapissl-conf %{buildroot}/etc/xapi/xapissl.conf

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ocaml/xe-cli/xe.opt %{buildroot}/%{_bindir}/xe
mkdir -p %{buildroot}/etc/bash_completion.d
install -m 0755 ocaml/xe-cli/bash-completion %{buildroot}/etc/bash_completion.d/xe

mkdir -p %{buildroot}/var/lib/xapi
mkdir -p %{buildroot}/etc/xapi/hook-scripts

mkdir -p %{buildroot}/etc/xcp
echo master > %{buildroot}/etc/xcp/pool.conf

%clean
rm -rf %{buildroot}

%post
[ ! -x /sbin/chkconfig ] || chkconfig --add xapi

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xapi stop > /dev/null 2>&1
  /sbin/chkconfig --del xapi
fi

%files
%defattr(-,root,root,-)
%{_sbindir}/xapi
/etc/init.d/xapi
%config(noreplace) /etc/xapi.conf
%config(noreplace) /etc/xapi/xapissl.conf
%config(noreplace) /etc/xcp/pool.conf
%{_libexecdir}/xapi/xapissl
%{_libexecdir}/xapi/pci-info
/etc/xapi/db.conf
/etc/xapi/hook-scripts
/var/lib/xapi

%files xe
%defattr(-,root,root,-)
%{_bindir}/xe
/etc/bash_completion.d/xe

%changelog








