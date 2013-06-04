Summary: vncterm tty to vnc utility
Name: vncterm
Version: 0.1
Release: 0
License: GPL
Group: System/Hypervisor
Source0: %{name}-%{version}.tar.gz
Patch0:  vncterm-1-fix-build
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xen-devel

%description
This package contains the vncterm utility
%prep
%setup -q -n vncterm-master-%{version}
%patch0 -p1

%build
%{__make}

%install
mkdir -p %{buildroot}%{_bindir}/
cp vncterm %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/vncterm

%changelog
* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Imported from vncterm/mk/vncterm.spec.in

