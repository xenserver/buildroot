Name:           xsiostat
Version:        0.2.0
Release:        1
Summary:        XenServer IO stat thingy
License:        LGPLv2.1
Group:          Development/Other
URL:            https://github.com/xenserver/xsiostat
Source0:        https://github.com/xenserver/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

%description
Simple XenServer IO stat thingy

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 xsiostat %{buildroot}/%{_sbindir}/xsiostat

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xsiostat

%changelog
* Tue Jun 19 2013 David Scott <dave.scott@eu.citrix.com> - 0.2.0-1
- Initial package

