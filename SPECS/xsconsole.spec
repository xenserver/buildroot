Summary: XenServer Host Configuration Console
Name: xsconsole
Version: 0.9.0
Release: 1
License: GPL2
Group: Administration/System
URL: http://github.com/jamesbulpin/xsconsole
Source0: https://github.com/jamesbulpin/xsconsole/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides: xsconsole0
Requires: PyPAM xapi-python-devel

%description
Console tool for configuring a XenServer installation.

%prep
%setup -q -n %{name}-%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib
make install-base DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

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
* Fri Jul 5 2013 James Bulpin <James.Bulpin@citrix.com> - 0.9.0-1
- Initial package

