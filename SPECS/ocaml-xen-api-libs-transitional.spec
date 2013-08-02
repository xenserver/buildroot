Name:           ocaml-xen-api-libs-transitional
Version:        0.9.0
Release:        1
Summary:        Deprecated standard library extension for OCaml.
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/xen-org/xen-api-libs-transitional
Source0:        https://github.com/xen-org/xen-api-libs-transitional/archive/xen-api-libs-transitional-%{version}/xen-api-libs-transitional-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-stdext-devel xmlm-devel forkexecd-devel
BuildRequires:  ocaml-rpc-devel ocaml-xen-lowlevel-libs-devel ocaml-xenstore-devel
BuildRequires:  ocaml-xenstore-clients-devel xen-devel ocaml-camlp4-devel
BuildRequires:  ocaml-syslog-devel
Requires:       ocaml ocaml-findlib xen-libs

%description
A deprecated standard library extension for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xen-api-libs-transitional-xen-api-libs-transitional-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md LICENSE
%{_libdir}/ocaml/cpuid/*
%{_libdir}/ocaml/gzip/*
%{_libdir}/ocaml/http-svr/*
%{_libdir}/ocaml/log/*
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
%{_libdir}/ocaml/stublibs/dlllog_stubs.so
%{_libdir}/ocaml/stublibs/dlllog_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxenctrlext_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrlext_stubs.so.owner

%changelog
* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

