# -*- rpm-spec -*-

Summary: command-line tools for manipulating and streaming .vhd format files
Name:    vhd-tool
Version: 0.6.1
Release: 1
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  https://github.com/djs55/vhd-tool
Source0: https://github.com/djs55/vhd-tool/archive/%{version}/vhd-tool-%{version}.tar.gz
Source1: vhd-tool-sparse_dd-conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc
BuildRequires: ocaml-xcp-idl-devel ocaml-vhd-devel ocaml-obuild
BuildRequires: ocaml-nbd-devel ocaml-cstruct-devel ocaml-lwt-devel
BuildRequires: ocaml-ounit-devel ocaml-rpc-devel ocaml-ssl-devel ocaml-stdext-devel
BuildRequires: ocaml-tapctl-devel ocaml-xen-lowlevel-libs-devel
BuildRequires: ocaml-xenstore-devel git cmdliner-devel ocaml-oclock-devel
BuildRequires: libuuid-devel
BuildRequires: ocaml-xenstore-clients-devel message-switch-devel
BuildRequires: openssl openssl-devel

%description
Simple command-line tools for manipulating and streaming .vhd format file.

%prep 
%setup -q
cp %{SOURCE1} vhd-tool-sparse_dd-conf


%build
./configure --bindir %{buildroot}/%{_bindir} --libexecdir %{buildroot}/%{_libexecdir}/xapi --etcdir %{buildroot}/etc
make

%install
rm -rf %{buildroot}
 
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/xapi
mkdir -p %{buildroot}/etc
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/vhd-tool
/etc/sparse_dd.conf
%{_libexecdir}/xapi/sparse_dd

%changelog
* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.1-1
- Update to 0.6.1

* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Update to 0.6.0

* Fri Sep 27 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.1-1
- Update to 0.5.1

* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.0-1
- Initial package
