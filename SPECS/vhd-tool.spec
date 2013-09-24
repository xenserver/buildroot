# -*- rpm-spec -*-

Summary: command-line tools for manipulating and streaming .vhd format files
Name:    vhd-tool
Version: 0.5.0
Release: 1
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: https://github.com/djs55/ocaml-vhd/archive/%{version}/ocaml-vhd-%{version}.tar.gz
Source1: vhd-tool-sparse_dd-conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc
BuildRequires: ocaml-xcp-idl-devel
BuildRequires: ocaml-nbd-devel ocaml-cstruct-devel ocaml-lwt-devel
BuildRequires: ocaml-ounit-devel ocaml-rpc-devel ocaml-ssl-devel ocaml-stdext-devel
BuildRequires: ocaml-syslog-devel ocaml-tapctl-devel ocaml-xen-lowlevel-libs-devel
BuildRequires: ocaml-xenstore-devel git cmdliner-devel ocaml-oclock-devel
BuildRequires: libuuid-devel make utop
BuildRequires: ocaml-xenstore-clients-devel message-switch-devel
BuildRequires: python2-devel

%description
Simple command-line tools for manipulating and streaming .vhd format file.

%prep 
%setup -q -n ocaml-vhd-%{version}
cp %{SOURCE1} vhd-tool-sparse_dd-conf


%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
 
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 main.native %{buildroot}/%{_sbindir}/vhd-tool
mkdir -p %{buildroot}/%{_libexecdir}
install -m 0755 sparse_dd.native %{buildroot}/%{_libexecdir}/xapi/sparse_dd
mkdir -p %{buildroot}/etc
install -m 0755 vhd-tool-sparse_dd-conf %{buildroot}/etc/sparse_dd.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/vhd-tool
/etc/sparse_dd.conf
%{_libexecdir}/xapi/sparse_dd

%changelog
* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.0-1
- Initial package
