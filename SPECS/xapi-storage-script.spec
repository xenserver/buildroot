# -*- rpm-spec -*-

Summary: Xapi storage script plugin server
Name:    xapi-storage-script
Version: 0.12.0
Release: 2%{?dist}
License: LGPL+linking exception
URL:     https://github.com/xapi-project/xapi-storage-script
Source0: https://github.com/xapi-project/xapi-storage-script/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: xapi-storage-script-init
Source2: xapi-storage-script-conf.in
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-xcp-idl-devel
BuildRequires: ocaml-async-inotify-devel
BuildRequires: message-switch-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: xapi-storage-devel
BuildRequires: ocaml-xcp-rrd-devel

%description
Allows script-based Xapi storage adapters.

%prep 
%setup -q -n %{name}-%{version}
cp %{SOURCE1} xapi-storage-script-init
cp %{SOURCE2} xapi-storage-script-conf.in

%build
make
mv main.native xapi-storage-script
./xapi-storage-script --help=groff > xapi-storage-script.1
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" xapi-storage-script-conf.in > xapi-storage-script.conf

%install
 
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 xapi-storage-script %{buildroot}/%{_sbindir}/xapi-storage-script
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xapi-storage-script-init %{buildroot}%{_sysconfdir}/init.d/xapi-storage-script
mkdir -p %{buildroot}/%{_libexecdir}/xapi-storage-script
mkdir -p %{buildroot}/%{_libexecdir}/xapi-storage-script/volume
mkdir -p %{buildroot}/%{_libexecdir}/xapi-storage-script/datapath
mkdir -p %{buildroot}/etc
install -m 0644 xapi-storage-script.conf %{buildroot}/etc/xapi-storage-script.conf
mkdir -p %{buildroot}%{_mandir}/man2
install -m 0644 xapi-storage-script.1 %{buildroot}%{_mandir}/man2/xapi-storage-script.1
gzip %{buildroot}%{_mandir}/man2/xapi-storage-script.1

%post
[ ! -x /sbin/chkconfig ] || chkconfig --add xapi-storage-script

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xapi-storage-script stop > /dev/null 2>&1
  /sbin/chkconfig --del xapi-storage-script
fi

%files
%{_sbindir}/xapi-storage-script
/etc/init.d/xapi-storage-script
%config(noreplace) /etc/xapi-storage-script.conf
%{_libexecdir}/xapi-storage-script
%{_libexecdir}/xapi-storage-script/volume
%{_libexecdir}/xapi-storage-script/datapath
%{_mandir}/man2/xapi-storage-script.1.gz

%changelog
* Tue Sep 15 2015 David Scott <dave.scott@citrix.com> - 0.12.0-2
- Bump release

* Wed Sep  9 2015 David Scott <dave.scott@citrix.com> - 0.12.0-1
- Update to 0.12.0

* Fri Aug  7 2015 David Scott <dave.scott@citrix.com> - 0.11.0-1
- Update to 0.11.0

* Tue Aug  5 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Mon Jul 20 2015 David Scott <dave.scott@citrix.com> - 0.9.0-2
- Backport robustness patch

* Thu Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.8.0-2
- Backport clone-on-boot fix

* Wed Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 9 2015 David Scott <dave.scott@citrix.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jul 8 2015 David Scott <dave.scott@citrix.com> - 0.6.0-1
- Update to 0.6.0

* Tue Jul 7 2015 David Scott <dave.scott@citrix.com> - 0.5.0-1
- Update to 0.5.0

* Tue Apr 28 2015 David Scott <dave.scott@citrix.com> - 0.4.0-1
- Update to 0.4.0

* Fri Apr 24 2015 David Scott <dave.scott@citrix.com> - 0.3.0-1
- Update to 0.3.0

* Sat Apr  4 2015 David Scott <dave.scott@citrix.com> - 0.2.0-1
- Update to 0.2.0

* Sun Oct 19 2014 David Scott <dave.scott@citrix.com> - 0.1.2-1
- Write the pidfile properly
- VDI.epoch_{begin,end} are no-ops

* Fri Oct 17 2014 David Scott <dave.scott@citrix.com> - 0.1.1-1
- Add the /volume and /datapath subdirectories to the package
- Fix daemonization
- Use syslog

* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
