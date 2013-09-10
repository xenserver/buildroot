Name:           ffs
Version:        0.9.17
Release:        1
Summary:        Simple flat file storage manager for the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/ffs/archive/%{version}.tar.gz
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        ffs-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-oclock-devel ocaml-libvhd-devel xen-devel libuuid-devel
BuildRequires:  ocaml-tapctl-devel message-switch-devel forkexecd-devel
Requires:       ocaml-libvhd-devel nfs-utils redhat-lsb-core

%description
Simple flat file storage manager for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} ffs-init

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/ffs/ffs %{buildroot}/%{_sbindir}/ffs
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 ffs-init %{buildroot}%{_sysconfdir}/init.d/ffs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/ffs
%{_sysconfdir}/init.d/ffs

%post
/sbin/chkconfig --add ffs

%preun
if [ $1 -eq 0 ]; then
  /sbin/service ffs stop > /dev/null 2>&1
  /sbin/chkconfig --del ffs
fi

%changelog
* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.17

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.4

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

