# -*- rpm-spec -*-

Summary: Xen toolstack for XCP
Name:    xapi
Version: 1.9.52
Release: 1%{?dist}
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: https://github.com/xapi-project/xen-api/archive/v%{version}/xen-api-%{version}.tar.gz
Source1: xen-api-xapi-conf.in
Source2: xen-api-init
Source3: xen-api-xapissl
Source4: xen-api-db-conf
Source5: xen-api-pam
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: pam-devel
BuildRequires: tetex-latex
BuildRequires: xen-devel
BuildRequires: libffi-devel
BuildRequires: zlib-devel
BuildRequires: ocaml-xcp-idl-devel
BuildRequires: ocaml-xen-api-libs-transitional-devel
BuildRequires: ocaml-netdev-devel
BuildRequires: ocaml-xen-api-client-devel
BuildRequires: omake
BuildRequires: forkexecd-devel
BuildRequires: ocaml-cdrom-devel
BuildRequires: ocaml-fd-send-recv-devel
BuildRequires: ocaml-libvhd-devel
BuildRequires: ocaml-nbd-devel
BuildRequires: ocaml-oclock-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: ocaml-ssl-devel
BuildRequires: ocaml-stdext-devel
BuildRequires: ocaml-tapctl-devel
BuildRequires: ocaml-xen-lowlevel-libs-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-opasswd-devel
BuildRequires: git
BuildRequires: ocaml-xcp-inventory-devel
BuildRequires: ocaml-xenstore-devel
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: utop
BuildRequires: message-switch-devel
BuildRequires: ocaml-xenstore-clients-devel
BuildRequires: ocaml-xcp-rrd-devel
BuildRequires: ocaml-tar-devel
BuildRequires: python2-devel
Requires: hwdata
Requires: ocaml-xcp-inventory
Requires: redhat-lsb-core
Requires: stunnel
Requires: vhd-tool
Requires: libffi

%description
XCP toolstack.

%description
This package contains the xapi toolstack.

%package xe
Summary: The xapi toolstack CLI
Requires: bash-completion

%description xe
The command-line interface for controlling XCP hosts.

%package python-devel
Summary: XenAPI client support in python
Requires: python

%description python-devel
Libraries for writing XenAPI clients in python.

%prep 
%setup -q -n xen-api-%{version}
cp %{SOURCE1} xen-api-xapi-conf.in
cp %{SOURCE2} xen-api-init
cp %{SOURCE3} xen-api-xapissl
cp %{SOURCE4} xen-api-db-conf
cp %{SOURCE5} xen-api-pam


%build
./configure --bindir=%{_bindir} --etcdir=/etc --libexecdir=%{_libexecdir}/xapi --xapiconf=/etc/xapi.conf --hooksdir=/etc/xapi/hook-scripts --sharedir=/usr/share/xapi --plugindir=/usr/lib/xapi/plugins --optdir=/usr/lib/xapi --disable-tests
make

sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" xen-api-xapi-conf.in > xen-api-xapi-conf

%install
 
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 ocaml/xapi/xapi.opt %{buildroot}/%{_sbindir}/xapi
mkdir -p %{buildroot}/etc/pam.d
install -m 0644 xen-api-pam %{buildroot}/etc/pam.d/xapi
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xen-api-init %{buildroot}%{_sysconfdir}/init.d/xapi
mkdir -p %{buildroot}/%{_libexecdir}/xapi
install -m 0755 xen-api-xapissl %{buildroot}/%{_libexecdir}/xapi/xapissl
install -m 0755 scripts/update-mh-info %{buildroot}/%{_libexecdir}/xapi/update-mh-info
mkdir -p %{buildroot}/etc/xapi
install -m 0644 xen-api-xapi-conf %{buildroot}/etc/xapi.conf
install -m 0644 xen-api-db-conf %{buildroot}/etc/xapi/db.conf

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ocaml/xe-cli/xe.opt %{buildroot}/%{_bindir}/xe
mkdir -p %{buildroot}/etc/bash_completion.d
install -m 0755 ocaml/xe-cli/bash-completion %{buildroot}/etc/bash_completion.d/xe

mkdir -p %{buildroot}/var/lib/xapi
mkdir -p %{buildroot}/etc/xapi/hook-scripts

mkdir -p %{buildroot}/etc/xcp
echo master > %{buildroot}/etc/xcp/pool.conf

mkdir -p %{buildroot}/usr/share/xapi/packages/iso

mkdir -p %{buildroot}%{python_sitelib}
install -m 0644 scripts/examples/python/XenAPI.py %{buildroot}%{python_sitelib}
install -m 0644 scripts/examples/python/XenAPIPlugin.py %{buildroot}%{python_sitelib}


%post
[ ! -x /sbin/chkconfig ] || chkconfig --add xapi

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xapi stop > /dev/null 2>&1
  /sbin/chkconfig --del xapi
fi

%files
%{_sbindir}/xapi
/etc/init.d/xapi
%config(noreplace) /etc/xapi.conf
%config(noreplace) /etc/xcp/pool.conf
%{_libexecdir}/xapi/xapissl
%{_libexecdir}/xapi/update-mh-info
/etc/xapi/db.conf
/etc/xapi/hook-scripts
/var/lib/xapi
/usr/share/xapi/packages/iso
/etc/pam.d/xapi

%files xe
%{_bindir}/xe
/etc/bash_completion.d/xe

%files python-devel
%{python_sitelib}/XenAPI.py
%{python_sitelib}/XenAPI.pyo
%{python_sitelib}/XenAPI.pyc

%{python_sitelib}/XenAPIPlugin.py
%{python_sitelib}/XenAPIPlugin.pyo
%{python_sitelib}/XenAPIPlugin.pyc

%changelog
* Tue Jul 29 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.9.52-1
- update 1.9.52

* Fri Jun  6 2014 David Scott <dave.scott@citrix.com> - 1.9.50-1
- update 1.9.50

* Fri May 23 2014 David Scott <dave.scott@citrix.com> - 1.9.49-1
- update to 1.9.49

* Tue May 13 2014 David Scott <dave.scott@citrix.com> - 1.9.47-1
- update to 1.9.47

* Sun May 11 2014 David Scott <dave.scott@citrix.com> - 1.9.46-1
- update to 1.9.46

* Sat May 10 2014 David Scott <dave.scott@citrix.com> - 1.9.45-1
- update to 1.9.45

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 1.9.44-1
- update to 1.9.44

* Mon Apr 28 2014 David Scott <dave.scott@citrix.com> - 1.9.41-1
- first release from master

* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 1.9.40-1
- update to new xcp-idl interface with SR.probe

* Wed Apr 2 2014 Euan Harris <euan.harris@citrix.com> - 1.9.39-1
- update to 1.9.39 - switch from stdext's Tar to ocaml-tar

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.38-1
- update to 1.9.38 - import_raw_vdi path fix

* Tue Oct 29 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.37-1
- update to 1.9.37 - bugfixes for storage motion on Ubuntu

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.36-1
- update to 1.9.36 - bugfixes for storage motion

* Tue Oct 22 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.34-1
- Update to 1.9.34 - bugfix for VDI.uuid filename feature

* Mon Oct 21 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.32-1
- Update to 1.9.32 - include VDI.uuid filename improvements

* Fri Oct 11 2013 Euan Harris <euan.harris@citrix.com> - 1.9.30-1
- Update to 1.9.30 - assume dom0 can be ballooned in all memory calculations.

* Fri Sep 27 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.29-1
- Update to 1.9.29

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 1.9.28

* Tue Sep 24 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.27-2
- Remove dependency on ocaml-bitstring

* Tue Sep 24 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.27-1
- Update to 1.9.27

* Thu Sep 19 2013 Euan Harris <euan.harris@citrix.com> - 1.9.25-2
- Use 'python_sitelib' macro to choose Python install path, instead of hard-coding it.

* Wed Sep 11 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.25-1
- Can now use either 'ffs' or 'iso' for the tools SR

* Wed Sep  4 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.22-1
- Query domain 0 memory policy from squeezed

* Wed Sep  4 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.21-1
- Update to 1.9.21, switch default xenopsd to the "classic" version

* Mon Sep  2 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.20-1
- Fix XenAPI.py on python2.7

* Tue Aug 20 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.19-1
- Add sparse_dd to the xapi package so VDI.copy should work

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.6-1
- Update to 1.9.6

* Sat Jun 8 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.2-1
- Add python-devel for writing python clients

* Wed Jun 5 2013 David Scott <dave.scott@eu.citrix.com> - 1.9.1-1
- Initial package

