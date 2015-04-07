Summary: Enhanced version of tapdisk
Name:    blktap
Version: 3.0.50
Release: 1%{?dist}
License: LGPL+linking exception
URL:  https://github.com/xapi-project/blktap
Source0: https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: blktap-gntcpy.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: xen-devel
BuildRequires: openssl-devel

%description
Enhanced version of tapdisk with support for storage mirroring.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep 
%setup -q
%patch0 -p1

%build
sh autogen.sh
./configure --prefix %{_libdir}/%{name} --disable-gcopy
make

%install

mkdir -p %{buildroot}/%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_libdir}/%{name}/lib
mkdir -p %{buildroot}/%{_libdir}/%{name}/sbin
mkdir -p %{buildroot}/%{_libdir}/%{name}/bin
mkdir -p %{buildroot}/%{_libdir}/%{name}/include/blktap
mkdir -p %{buildroot}/%{_libdir}/%{name}/include/vhd
mkdir -p %{buildroot}/%{_libdir}/%{name}/libexec
mkdir -p %{buildroot}/%{_libdir}/%{name}/etc/udev/rules.d

make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/usr/include/blktap
mv %{buildroot}/%{_libdir}/%{name}/include/blktap/blktap3.h %{buildroot}/usr/include/blktap

%files
%{_libdir}/%{name}/bin/*
%{_libdir}/%{name}/etc/udev/rules.d/blktap.rules
%{_libdir}/%{name}/etc/logrotate.d/blktap
%{_libdir}/%{name}/etc/rc.d/init.d/tapback
%{_libdir}/%{name}/etc/xensource/bugtool/tapdisk-logs.xml
%{_libdir}/%{name}/etc/xensource/bugtool/tapdisk-logs/description.xml
%{_libdir}/%{name}/include/blktap/*
%{_libdir}/%{name}/include/vhd/*
%{_libdir}/%{name}/lib/*
%{_libdir}/%{name}/libexec/*
%{_libdir}/%{name}/sbin/*

%files devel
/usr/include/blktap/*

%changelog
* Tue Apr 7 2015 David Scott <dave.scott@citrix.com> - 3.0.50-1
- Update to 3.0.50

* Thu Feb 5 2015 David Scott <dave.scott@citrix.com> - 0.9.3.fe874d-2
- Fix the build on 32-bit machines

* Mon Dec 8 2014 Bob Ball <bob.ball@citrix.com> - 0.9.3.fe874d-1
- Update to Creedence branch without grantcopy
- Using checkpoint off xs64bit branch until an official release is made

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.2-2
- Remove xen-missing-headers dependency

* Wed Jun 04 2014 Bob Ball <bob.ball@citrix.com> - 0.9.2-1
- Update blktap to latest release

* Wed Mar 12 2014 Bob Ball <bob.ball@citrix.com> - 0.9.1-1
- Update blktap to avoid Debian Jessie compile failure 

* Fri Jan 17 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Change to upstream source repository

* Thu Oct 24 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package
