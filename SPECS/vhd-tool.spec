# -*- rpm-spec -*-

Summary: Command-line tools for manipulating and streaming .vhd format files
Name:    vhd-tool
Version: 0.7.5
Release: 1%{?dist}
License: LGPL+linking exception
URL:  https://github.com/xapi-project/vhd-tool
Source0: https://github.com/xapi-project/vhd-tool/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: vhd-tool-sparse_dd-conf
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-vhd-devel
BuildRequires: ocaml-xcp-idl-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-nbd-devel
BuildRequires: ocaml-tapctl-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-xenstore-devel
BuildRequires: ocaml-io-page-devel
BuildRequires: ocaml-sha-devel
BuildRequires: ocaml-tar-devel
BuildRequires: ocaml-xenstore-clients-devel

%description
Simple command-line tools for manipulating and streaming .vhd format file.

%prep 
%setup -q
cp %{SOURCE1} vhd-tool-sparse_dd-conf


%build
./configure --bindir %{buildroot}/%{_bindir} --libexecdir %{buildroot}/%{_libexecdir}/xapi --etcdir %{buildroot}/etc
make

%install
 
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/xapi
mkdir -p %{buildroot}/etc
make install


%files
%{_bindir}/vhd-tool
/etc/sparse_dd.conf
%{_libexecdir}/xapi/sparse_dd

%changelog
* Fri Jun 6 2014 Jonathan Ludlam <jonathan.ludlam@citrix.com> - 0.7.5-1
- Update to 0.7.5

* Wed Apr 9 2014 Euan Harris <euan.harris@citrix.com> - 0.7.4-1
- Update to 0.7.4 - fix handling of tar file prefixes

* Wed Apr 2 2014 Euan Harris <euan.harris@citrix.com> - 0.7.3-1
- Update to 0.7.3

* Thu Nov 21 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.4-1
- Update to 0.6.4

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.1-1
- Update to 0.6.1

* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Update to 0.6.0

* Fri Sep 27 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.1-1
- Update to 0.5.1

* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.0-1
- Initial package
