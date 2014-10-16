# -*- rpm-spec -*-

Summary: Xapi storage script plugin server
Name:    xapi-storage-script
Version: 0.1
Release: 1%{?dist}
License: LGPL+linking exception
URL:     https://github.com/djs55/xapi-storage-script
Source0: https://github.com/djs55/xapi-storage-script/archive/v%{version}/%{name}-%{version}.tar.gz
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
%{_mandir}/man2/xapi-storage-script.1.gz

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
