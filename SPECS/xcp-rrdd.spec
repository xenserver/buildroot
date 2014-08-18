Name:           xcp-rrdd
Version:        0.9.7
Release:        1%{?dist}
Summary:        Statistics gathering daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xcp-rrdd
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        xcp-rrdd-init
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xenops-devel
BuildRequires:  ocaml-rrd-transport-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  forkexecd-devel
BuildRequires:  xen-devel
BuildRequires:  xen-missing-headers
Requires:       redhat-lsb-core

%description
Statistics gathering daemon for the xapi toolstack.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-xcp-idl-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

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
%{_libdir}/ocaml/rrdd-libs
%exclude %{_libdir}/ocaml/rrdd-libs/*.a
%exclude %{_libdir}/ocaml/rrdd-libs/*.cmx
%exclude %{_libdir}/ocaml/rrdd-libs/*.cmxa
%exclude %{_libdir}/ocaml/rrdd-libs/*.mli

%files devel
%{_libdir}/ocaml/rrdd-libs/*.a
%{_libdir}/ocaml/rrdd-libs/*.cmx
%{_libdir}/ocaml/rrdd-libs/*.cmxa
%{_libdir}/ocaml/rrdd-libs/*.mli

%post
/sbin/chkconfig --add xcp-rrdd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-rrdd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-rrdd
fi

%changelog
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

