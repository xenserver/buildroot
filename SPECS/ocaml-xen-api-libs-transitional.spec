%global debug_package %{nil}

Name:           ocaml-xen-api-libs-transitional
Version:        0.9.9
Release:        1%{?dist}
Summary:        Deprecated standard library extension for OCaml
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/xen-api-libs-transitional
Source0:        https://github.com/xapi-project/xen-api-libs-transitional/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xmlm-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  xen-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-backtrace-devel
BuildRequires:  oasis
Requires:       xen-libs

%description
A deprecated standard library extension for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xen-api-libs-transitional-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=$OCAMLFIND_DESTDIR

%files
%doc ChangeLog 
%doc LICENSE
%doc README.md 

%{_libdir}/ocaml/gzip
%exclude %{_libdir}/ocaml/gzip/*.a
%exclude %{_libdir}/ocaml/gzip/*.cmxa
%exclude %{_libdir}/ocaml/gzip/*.cmx
%exclude %{_libdir}/ocaml/gzip/*.mli

%{_libdir}/ocaml/http-svr
%exclude %{_libdir}/ocaml/http-svr/*.a
%exclude %{_libdir}/ocaml/http-svr/*.cmxa
%exclude %{_libdir}/ocaml/http-svr/*.cmx
%exclude %{_libdir}/ocaml/http-svr/*.mli

%{_libdir}/ocaml/pciutil
%exclude %{_libdir}/ocaml/pciutil/*.a
%exclude %{_libdir}/ocaml/pciutil/*.cmxa
%exclude %{_libdir}/ocaml/pciutil/*.cmx
%exclude %{_libdir}/ocaml/pciutil/*.mli

%{_libdir}/ocaml/sexpr
%exclude %{_libdir}/ocaml/sexpr/*.a
%exclude %{_libdir}/ocaml/sexpr/*.cmxa
%exclude %{_libdir}/ocaml/sexpr/*.cmx
%exclude %{_libdir}/ocaml/sexpr/*.mli

%{_libdir}/ocaml/sha1
%exclude %{_libdir}/ocaml/sha1/*.a
%exclude %{_libdir}/ocaml/sha1/*.cmxa
%exclude %{_libdir}/ocaml/sha1/*.cmx
%exclude %{_libdir}/ocaml/sha1/*.mli

%{_libdir}/ocaml/stunnel
%exclude %{_libdir}/ocaml/stunnel/*.a
%exclude %{_libdir}/ocaml/stunnel/*.cmxa
%exclude %{_libdir}/ocaml/stunnel/*.cmx
%exclude %{_libdir}/ocaml/stunnel/*.mli

%{_libdir}/ocaml/uuid
%exclude %{_libdir}/ocaml/uuid/*.a
%exclude %{_libdir}/ocaml/uuid/*.cmxa
%exclude %{_libdir}/ocaml/uuid/*.cmx
%exclude %{_libdir}/ocaml/uuid/*.mli

%{_libdir}/ocaml/xenctrlext
%exclude %{_libdir}/ocaml/xenctrlext/*.a
%exclude %{_libdir}/ocaml/xenctrlext/*.cmxa
%exclude %{_libdir}/ocaml/xenctrlext/*.cmx
%exclude %{_libdir}/ocaml/xenctrlext/*.mli
%{_libdir}/ocaml/stublibs/dllxenctrlext_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrlext_stubs.so.owner

%{_libdir}/ocaml/xenstore-compat
%exclude %{_libdir}/ocaml/xenstore-compat/*.a
%exclude %{_libdir}/ocaml/xenstore-compat/*.cmxa
%exclude %{_libdir}/ocaml/xenstore-compat/*.cmx

%{_libdir}/ocaml/xml-light2
%exclude %{_libdir}/ocaml/xml-light2/*.a
%exclude %{_libdir}/ocaml/xml-light2/*.cmxa
%exclude %{_libdir}/ocaml/xml-light2/*.cmx
%exclude %{_libdir}/ocaml/xml-light2/*.mli


%files devel
%{_libdir}/ocaml/gzip/*.a
%{_libdir}/ocaml/gzip/*.cmxa
%{_libdir}/ocaml/gzip/*.cmx
%{_libdir}/ocaml/gzip/*.mli

%{_libdir}/ocaml/http-svr/*.a
%{_libdir}/ocaml/http-svr/*.cmxa
%{_libdir}/ocaml/http-svr/*.cmx
%{_libdir}/ocaml/http-svr/*.mli

%{_libdir}/ocaml/pciutil/*.a
%{_libdir}/ocaml/pciutil/*.cmxa
%{_libdir}/ocaml/pciutil/*.cmx
%{_libdir}/ocaml/pciutil/*.mli

%{_libdir}/ocaml/sexpr/*.a
%{_libdir}/ocaml/sexpr/*.cmxa
%{_libdir}/ocaml/sexpr/*.cmx
%{_libdir}/ocaml/sexpr/*.mli

%{_libdir}/ocaml/sha1/*.a
%{_libdir}/ocaml/sha1/*.cmxa
%{_libdir}/ocaml/sha1/*.cmx
%{_libdir}/ocaml/sha1/*.mli

%{_libdir}/ocaml/stunnel/*.a
%{_libdir}/ocaml/stunnel/*.cmxa
%{_libdir}/ocaml/stunnel/*.cmx
%{_libdir}/ocaml/stunnel/*.mli

%{_libdir}/ocaml/uuid/*.a
%{_libdir}/ocaml/uuid/*.cmxa
%{_libdir}/ocaml/uuid/*.cmx
%{_libdir}/ocaml/uuid/*.mli

%{_libdir}/ocaml/xenctrlext/*.a
%{_libdir}/ocaml/xenctrlext/*.cmxa
%{_libdir}/ocaml/xenctrlext/*.cmx
%{_libdir}/ocaml/xenctrlext/*.mli

%{_libdir}/ocaml/xenstore-compat/*.a
%{_libdir}/ocaml/xenstore-compat/*.cmxa
%{_libdir}/ocaml/xenstore-compat/*.cmx

%{_libdir}/ocaml/xml-light2/*.a
%{_libdir}/ocaml/xml-light2/*.cmxa
%{_libdir}/ocaml/xml-light2/*.cmx
%{_libdir}/ocaml/xml-light2/*.mli

%changelog
* Fri Dec 11 2015 Euan Harris <euan.harris@citrix.com> - 0.9.9-1
- Remove cpuid
- Remove xen-utils

* Wed Sep 9 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.8-2
- Bump release

* Thu Aug 20 2015 David Scott <dave.scott@citrix.com> - 0.9.8-1
- Update to 0.9.8

* Wed Jan 21 2015 David Scott <dave.scott@citrix.com> - 0.9.7-1
- Update to 0.9.7

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-2
- Remove xen-missing-headers dependency

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-1
- Update to 0.9.6 release

* Mon Jun 2 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Split files correctly between base and devel packages

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Update to 0.9.3

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

