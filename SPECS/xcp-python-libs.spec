%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Common XenServer Python classes
Name: xcp-python-libs
Version: 0.9.0
Release: 1
Source: https://github.com/euanh/python-libs/archive/%{version}/%{name}-%{version}.tar.gz
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: python-devel python-setuptools

%description
Common XenServer Python classes.

%prep
%setup -q -n python-libs-%{version}

%build
mkdir -p xcp
cp *.py xcp
cp -r net xcp
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O2 --skip-build --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}


%changelog
* Thu Jan 23 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-1
- Initial package

