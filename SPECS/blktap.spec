Summary: Enhanced version of tapdisk
Name:    blktap
Version: 0.9.0
Release: 1
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  https://github.com/djs55/blktap
Source0: https://github.com/djs55/blktap/archive/%{version}/blktap-%{version}.tar.gz
BuildRequires: autoconf automake libtool libaio-devel xen-devel libuuid-devel

%description
Enhanced version of tapdisk with support for storage mirroring.

%prep 
%setup -q


%build
sh autogen.sh
./configure --prefix %{_libdir}/%{name}
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


%files
%{_libdir}/%{name}/bin/*
%{_libdir}/%{name}/etc/udev/rules.d/blktap.rules
%{_libdir}/%{name}/include/blktap/*
%{_libdir}/%{name}/include/vhd/*
%{_libdir}/%{name}/lib/*
%{_libdir}/%{name}/libexec/*
%{_libdir}/%{name}/sbin/*

%changelog
* Thu Oct 24 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package
