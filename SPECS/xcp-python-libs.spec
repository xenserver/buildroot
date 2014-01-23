Summary: Common XenServer Python classes
Name: xcp-python-libs
Version: 0.9.0
Release: 1
URL: https://github.com/xenserver/python-libs
Source: https://github.com/euanh/python-libs/archive/%{version}/%{name}-%{version}.tar.gz
License: GPL
Group: Applications/System
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
%{__python} setup.py install -O2 --skip-build --root %{buildroot}
rm -rf %{buildroot}/%{python_sitelib}/*-py*.egg-info

%files
%{python_sitelib}/xcp


%changelog
* Thu Jan 23 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-1
- Initial package

