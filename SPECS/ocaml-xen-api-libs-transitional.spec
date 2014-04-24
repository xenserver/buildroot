%global debug_package %{nil}

Name:           ocaml-xen-api-libs-transitional
Version:        0.9.3
Release:        1%{?dist}
Summary:        Deprecated standard library extension for OCaml
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Libraries
URL:            http://github.com/xapi-project/xen-api-libs-transitional
Source0:        https://github.com/xapi-project/xen-api-libs-transitional/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdext-devel
BuildRequires:  xmlm-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  xen-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-xcp-idl-devel
Requires:       xen-libs

%description
A deprecated standard library extension for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xen-api-libs-transitional-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml


%files
#This space intentionally left blank

%files devel
%doc ChangeLog README.md LICENSE
%{_libdir}/ocaml/cpuid/*
%{_libdir}/ocaml/gzip/*
%{_libdir}/ocaml/http-svr/*
%{_libdir}/ocaml/pciutil/*
%{_libdir}/ocaml/sexpr/*
%{_libdir}/ocaml/sha1/*
%{_libdir}/ocaml/stunnel/*
%{_libdir}/ocaml/uuid/*
%{_libdir}/ocaml/xenctrlext/*
%{_libdir}/ocaml/xenstore-compat/*
%{_libdir}/ocaml/xen-utils/*
%{_libdir}/ocaml/xml-light2/*
%{_libdir}/ocaml/stublibs/dllcpuid_stubs.so
%{_libdir}/ocaml/stublibs/dllcpuid_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxenctrlext_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrlext_stubs.so.owner

%changelog
* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Update to 0.9.3

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

