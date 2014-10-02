Name:           ffs
Version:        0.9.25
Release:        1%{?dist}
Summary:        Simple flat file storage manager for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/ffs
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        ffs-init
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-vhd-devel
BuildRequires:  ocaml-tapctl-devel
Requires:       nfs-utils
Requires:       redhat-lsb-core
Requires:       blktap

%description
Simple flat file storage manager for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} ffs-init

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_mandir}/man1
make install DESTDIR=%{buildroot} SBINDIR=%{_sbindir} MANDIR=%{_mandir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 ffs-init %{buildroot}%{_sysconfdir}/init.d/ffs


%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/ffs
%{_mandir}/man1/ffs.1.gz
%{_sysconfdir}/init.d/ffs

%post
/sbin/chkconfig --add ffs

%preun
if [ $1 -eq 0 ]; then
  /sbin/service ffs stop > /dev/null 2>&1
  /sbin/chkconfig --del ffs
fi

%changelog
* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.9.25-1
- Update to 0.9.25

* Thu Jan 16 2014 Euan Harris <euan.harris@citrix.com> - 0.9.24-1
- Update to 0.9.24, with VDI.clone fix

* Thu Oct 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.23-1
- Update to 0.9.23, with VDI.copy fix

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.22, with VDI.clone and VDI.snapshot fixes

* Mon Oct 28 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.21, with minimal storage motion support

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.20
- Detect a parallel install of blktap and use that

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.18

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.17

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.4

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

