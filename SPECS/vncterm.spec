Summary: vncterm tty to vnc utility
Name: vncterm
Version: 0.1
Release: 1
License: GPL
Group: System/Hypervisor
Source0: https://github.com/xen-org/%{name}/archive/master/%{version}/%{name}-%{version}.tar.gz
Patch0:  vncterm-1-fix-build
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xen-devel

%description
This package contains the vncterm utility
%prep
%setup -q -n %{name}-master-%{version}
%patch0 -p1

%build
%{__make}

%install
mkdir -p %{buildroot}%{_bindir}/
cp vncterm %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%pre
getent group vncterm >/dev/null || groupadd -r vncterm
getent group vncterm_base >/dev/null || groupadd -r vncterm_base
getent passwd vncterm >/dev/null || useradd -r -g vncterm -d /none -s /sbin/nologin -c 'for vncterm' vncterm
getent passwd vncterm_base >/dev/null || useradd -r -g vncterm_base -d /none -s /sbin/nologin -c 'for vncterm' vncterm_base

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/vncterm

%changelog
* Thu Jun 27 2013 David Scott <dave.scott@eu.citrix.com>
- add users and groups: vncterm,vncterm_base

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Imported from vncterm/mk/vncterm.spec.in

