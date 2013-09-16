Summary: XenServer Host Configuration Console
Name: xsconsole
Version: 0.9.0
Release: 2
License: GPL2
Group: Administration/System
URL: http://github.com/jamesbulpin/xsconsole
Source0: https://github.com/jamesbulpin/xsconsole/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides: xsconsole0
Requires: PyPAM xapi-python-devel

%description
Console tool for configuring a XenServer installation.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
make install-base DESTDIR=%{buildroot} LIBDIR=%{buildroot}/%{_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/xsconsole/*.py
%{_libdir}/xsconsole/*.pyc
%{_libdir}/xsconsole/*.pyo
%{_libdir}/xsconsole/plugins-base
#%{_libdir}/xsconsole/plugins-oem
#%{_libdir}/xsconsole/plugins-extras
%{_bindir}/xsconsole
%doc LICENSE

%changelog
* Mon Sep 16 2013 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Use %{_libdir} rather than hard coding library installation path

* Fri Jul 5 2013 James Bulpin <James.Bulpin@citrix.com> - 0.9.0-1
- Initial package

