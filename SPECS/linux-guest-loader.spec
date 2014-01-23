Summary: Bootloader for EL-based distros that support Xen
Name: linux-guest-loader
Version: 0.9.1
Release: 1
URL: https://github.com/xenserver/linux-guest-loader
Source0: https://github.com/mcclurmc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPL
Group: Applications/System
BuildArch: noarch
BuildRequires: python-devel python-setuptools
Requires: xcp-python-libs

%description
Bootloader for EL-based distros that support Xen.

%prep
%setup -q

%build
%{__python} setup.py build

%install
mkdir -p %{buildroot}/%{_sbindir}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-scripts %{_sbindir}
ln -s %{_sbindir}/eliloader.py %{buildroot}/%{_sbindir}/eliloader
rm -rf %{buildroot}/%{python_sitelib}/*-py*.egg-info
 
%files
%{_sbindir}/eliloader
%{_sbindir}/eliloader.py

%changelog
* Wed Jan 22 2014 Mike McClurg <mike.mcclurg@citrix.com> - 0.9.1-1
- Convert package from eliloader to upstream linux-guest-loader.

* Mon Jun 24 2013 David Scott <dave.scott@eu.citrix.com> - 0.3-1
- Update to eliloader 0.3

* Sat Jun 22 2013 David Scott <dave.scott@eu.citrix.com> - 0.2-1
- Update to eliloader 0.2 (doesn't assume data file directory is present)

* Sat Jun 22 2013 David Scott <dave.scott@eu.citrix.com> - 0.1-1
- Initial package

