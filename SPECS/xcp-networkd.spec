Name:           xcp-networkd
Version:        0.9.5
Release:        1%{?dist}
Summary:        Simple host network management service for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xcp-networkd
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        xcp-networkd-init
Source2:        xcp-networkd-conf
Source3:        xcp-networkd-network-conf
Source4:        xcp-networkd-bridge-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  libffi-devel
BuildRequires:  ocaml-netlink-devel
Requires:       ethtool
Requires:       redhat-lsb-core
Requires:       libffi-devel
Requires:       libnl3

%description
Simple host networking management service for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} xcp-networkd-init
cp %{SOURCE2} xcp-networkd-conf
cp %{SOURCE3} xcp-networkd-network-conf
cp %{SOURCE4} xcp-networkd-bridge-conf

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_bindir}
make install DESTDIR=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xcp-networkd-init %{buildroot}%{_sysconfdir}/init.d/xcp-networkd
mkdir -p %{buildroot}/etc/xcp
install -m 0644 xcp-networkd-network-conf %{buildroot}/etc/xcp/network.conf
install -m 0644 xcp-networkd-conf %{buildroot}/etc/xcp-networkd.conf
mkdir -p %{buildroot}/etc/modprobe.d
install -m 0644 xcp-networkd-bridge-conf %{buildroot}/etc/modprobe.d/bridge.conf
mkdir -p %{buildroot}%{_mandir}/man1
cp xcp-networkd.1 %{buildroot}%{_mandir}/man1/xcp-networkd.1
gzip %{buildroot}%{_mandir}/man1/xcp-networkd.1

%files
%doc README.markdown LICENSE MAINTAINERS
%{_sbindir}/xcp-networkd
%{_bindir}/networkd_db
%{_sysconfdir}/init.d/xcp-networkd
/etc/modprobe.d/bridge.conf
%config(noreplace) /etc/xcp/network.conf
%config(noreplace) /etc/xcp-networkd.conf
%{_mandir}/man1/xcp-networkd.1.gz

%post
/sbin/chkconfig --add xcp-networkd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-networkd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-networkd
fi

%changelog
* Sat Sep 27 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5 (now uses libnl)

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.4-1
- Update to 0.9.4
- Add networkd_db CLI

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Update to 0.9.3

* Wed Aug 28 2013 David Scott <dave.scott@eu.citrix.com>
- When loading the bridge module, prevent guest traffic being
  processed by the domain 0 firewall

* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Fri Jun  7 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

