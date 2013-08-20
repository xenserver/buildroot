Name:           xcp-networkd
Version:        0.9.2
Release:        1
Summary:        Simple host network management service for the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xcp-networkd/archive/xcp-networkd-%{version}.tar.gz
Source0:        https://github.com/xapi-project/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        xcp-networkd-init
Source2:        xcp-networkd-conf
Source3:        xcp-networkd-network-conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel forkexecd-devel ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-xcp-inventory-devel ocaml-ounit-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  ocaml-oclock-devel

%description
Simple host networking management service for the xapi toolstack.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} xcp-networkd-init
cp %{SOURCE2} xcp-networkd-conf
cp %{SOURCE3} xcp-networkd-network-conf

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/xcp-networkd/xcp-networkd %{buildroot}/%{_sbindir}/xcp-networkd
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xcp-networkd-init %{buildroot}%{_sysconfdir}/init.d/xcp-networkd
mkdir -p %{buildroot}/etc/xcp
install -m 0644 xcp-networkd-network-conf %{buildroot}/etc/xcp/network.conf
install -m 0644 xcp-networkd-conf %{buildroot}/etc/xcp-networkd.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.markdown LICENSE MAINTAINERS
%{_sbindir}/xcp-networkd
%{_sysconfdir}/init.d/xcp-networkd
%config(noreplace) /etc/xcp/network.conf
%config(noreplace) /etc/xcp-networkd.conf

%post
/sbin/chkconfig --add xcp-networkd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-networkd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-networkd
fi

%changelog
* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Fri Jun  7 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

