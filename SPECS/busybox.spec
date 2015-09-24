Name: busybox
Version: 1.23.2
Release: 1
Summary: Busybox binary providing simplified versions of system commands
License: GPL
Source0: http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.

%prep
%setup -q

%build
make defconfig
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/bin
install -m 755 busybox $RPM_BUILD_ROOT/bin/busybox

%clean
rm -rf $RPM_BUILD_ROOT

%files
/bin/busybox

%changelog
* Thu Sep 24 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.23.2-1
- New upstream release
- Minor fixes to the SPEC file

* Tue Oct  7 2014 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.22.1-1
- Initial packaging
