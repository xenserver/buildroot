Name:           xcp-rrdd
Version:        0.11.0
Release:        1%{?dist}
Summary:        Statistics gathering daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xcp-rrdd
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        xcp-rrdd-init
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xenops-devel
BuildRequires:  ocaml-rrd-transport-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-backtrace-devel
BuildRequires:  forkexecd-devel
BuildRequires:  xen-devel
BuildRequires:  blktap-devel
Requires:       redhat-lsb-core

%description
Statistics gathering daemon for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} xcp-rrdd-init

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install DESTDIR=%{buildroot} SBINDIR=%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xcp-rrdd-init %{buildroot}%{_sysconfdir}/init.d/xcp-rrdd


%files
%doc README.markdown LICENSE
%{_sbindir}/xcp-rrdd
%{_sysconfdir}/init.d/xcp-rrdd

%post
/sbin/chkconfig --add xcp-rrdd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-rrdd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-rrdd
fi

%changelog
* Fri Aug 14 2015 David Scott <dave.scott@citrix.com> - 0.11.0-1
- Update to 0.11.0

* Tue Apr  7 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 21 2015 David Scott <dave.scott@citrix.com> - 0.9.9-1
- Update to 0.9.9

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 0.9.8-1
- Update to 0.9.8

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-2
- Remove xen-missing-headers dependency 

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-1
- Update to 0.9.7
- Create new subpackage for the devel libraries now installed

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5, now will start without xen

* Sat Apr 26 2014 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update to 0.9.4, now depends on rrdd-transport

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

