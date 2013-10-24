Summary: enhanced version of tapdisk
Name:    blktap
Version: 0.9.0
Release: 1
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: https://github.com/djs55/blktap/archive/%{version}/blktap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: autoconf automake libtool libaio-devel xen-devel libuuid-devel

%description
Enhanced version of tapdisk with support for storage mirroring.

%prep 
%setup -q


%build
sh autogen.sh
./configure --prefix %{buildroot}/%{_libdir}/%{name}
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_libdir}/%{name}/lib
mkdir -p %{buildroot}/%{_libdir}/%{name}/sbin
mkdir -p %{buildroot}/%{_libdir}/%{name}/bin
mkdir -p %{buildroot}/%{_libdir}/%{name}/include/blktap
mkdir -p %{buildroot}/%{_libdir}/%{name}/include/vhd
mkdir -p %{buildroot}/%{_libdir}/%{name}/libexec
mkdir -p %{buildroot}/%{_libdir}/%{name}/etc/udev/rules.d

make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
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
