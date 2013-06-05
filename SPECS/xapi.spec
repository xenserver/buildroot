# -*- rpm-spec -*-

Summary: xapi - xen toolstack for XCP
Name:    xapi
Version: 1.9.0
Release: 0
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: xen-api-%{version}.tar.gz
Source1: xen-api-xapi-conf
Source2: xen-api-init
Source3: xen-api-xapissl
Source4: xen-api-xapissl-conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires: pam-devel tetex-latex ocaml xen-devel zlib-devel
BuildRequires: ocaml-xcp-idl-devel ocaml-xen-api-libs-transitional-devel
BuildRequires: ocaml-xen-api-client-devel omake ocaml-netdev-devel
BuildRequires: ocaml-cdrom-devel ocaml-fd-send-recv-devel forkexec-devel
BuildRequires: ocaml-libvhd-devel ocaml-nbd-devel ocaml-oclock-devel
BuildRequires: ocaml-ounit-devel ocaml-rpc-devel ocaml-ssl-devel ocaml-stdext-devel
BuildRequires: ocaml-syslog-devel ocaml-tapctl-devel ocaml-xen-lowlevel-libs-devel
BuildRequires: ocaml-xenstore-devel
Requires: stunnel

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
export COMPILE_JAVA=no
omake phase1
omake phase2
omake ocaml/xapi/xapi

%install
rm -rf %{buildroot}

mkdir %{buildroot}/%{_bindir}
install -m 0755 ocaml/xapi/xapi.opt %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/xen-api-init %{buildroot}%{_sysconfdir}/init.d/xapi
mkdir %{buildroot}/%{_libexecdir}/xapi
install -m 0755 %{_sourcedir}/xen-api-xapissl %{buildroot}/%{_libexecdir}/xapi/xapissl
mkdir %{buildroot}/etc/xapi
install -m 0644 db.conf %{buildroot}/etc/xapi
install -m 0644 ${_sourcedir}/xen-api-xapissl-conf %{buildroot}/etc/xapi/xapissl.conf

install -m 0755 ocaml/xe-cli/xe.opt %{buildroot}/%{_bindir}/xe
mkdir %{buildroot}/etc/bash_completion.d
install -m 0755 ocaml/xe-cli/bash-completion %{buildroot}/etc/bash_completion.d/xe

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
%{_bindir}/xapi
%config(noreplace) /etc/xapi.conf
%{_libexecdir}/xapi/xapissl
/etc/xapi/db.conf

%files xe
%defattr(-,root,root,-)
%{_bindir}/xe
/etc/bash_completion.d/xe

%changelog








