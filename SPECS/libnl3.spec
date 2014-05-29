Summary: Convenience library for kernel netlink sockets
License: LGPLv2
Name: libnl3
Version: 3.2.22
Release: 1%{?dist}
URL: http://www.infradead.org/~tgr/libnl/
Source: http://www.infradead.org/~tgr/libnl/files/libnl-%{version}.tar.gz
Source1: http://www.infradead.org/~tgr/libnl/files/libnl-doc-%{version}.tar.gz
BuildRequires: bison
BuildRequires: flex
BuildRequires: python

%description
This package contains a convenience library to simplify
using the Linux kernel's netlink sockets interface for
network manipulation

%package devel
Summary: Libraries and headers for using libnl3
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cli = %{version}-%{release}
Requires: kernel-headers

%description devel
This package contains various headers for using libnl3

%package cli
Summary: Command line interface utils for libnl3
Requires: %{name} = %{version}-%{release}

%description cli
This package contains various libnl3 utils and additional
libraries on which they depend

%package doc
Summary: API documentation for libnl3
Requires: %{name} = %{version}-%{release}

%description doc
This package contains libnl3 API documentation

%prep
%setup -q -n libnl-%{version}

tar -xzf %SOURCE1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la -delete

%post -p /sbin/ldconfig
%post cli -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%postun cli -p /sbin/ldconfig

%files
%doc COPYING
%exclude %{_libdir}/libnl-cli*.so.*
%{_libdir}/libnl-*.so.*
%config(noreplace) %{_sysconfdir}/*

%files devel
%doc COPYING
%{_includedir}/libnl3/netlink/
%dir %{_includedir}/libnl3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files cli
%doc COPYING
%{_libdir}/libnl-cli*.so.*
%{_libdir}/libnl/
%{_sbindir}/*
%{_mandir}/man8/* 

%files doc
%doc COPYING
%doc libnl-doc-%{version}/*.html
%doc libnl-doc-%{version}/*.css
%doc libnl-doc-%{version}/stylesheets/*
%doc libnl-doc-%{version}/images/*
%doc libnl-doc-%{version}/images/icons/*
%doc libnl-doc-%{version}/images/icons/callouts/*
%doc libnl-doc-%{version}/api/*

%changelog
* Thu Jul 04 2013 Simon Rowe <simon.rowe@eu.citrix.com> - 3.2.22-1
- Package for CentOS (derived from Fedora)
