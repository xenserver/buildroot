Name:           xcp-networkd
Version:        0.9.0
Release:        0
Summary:        Simple host network management service for the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xcp-networkd/archive/xcp-networkd-0.9.0.tar.gz
Source0:        xcp-networkd-0.9.0.tar.gz
Source1:        xcp-networkd-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel forkexec-devel ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-xcp-inventory-devel ocaml-ounit-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  ocaml-oclock-devel

%description
Simple host networking management service for the xapi toolstack.

%prep
%setup -q -n xcp-networkd-xcp-networkd-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/xcp-networkd/xcp-networkd %{buildroot}/%{_sbindir}/xcp-networkd
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/xcp-networkd-init %{buildroot}%{_sysconfdir}/init.d/xcp-networkd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.markdown LICENSE MAINTAINERS
%{_sbindir}/xcp-networkd
%{_sysconfdir}/init.d/xcp-networkd

%post
/sbin/chkconfig --add xcp-networkd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-networkd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-networkd
fi

%changelog
* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

