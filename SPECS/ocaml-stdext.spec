%global debug_package %{nil}

Name:           ocaml-stdext
Version:        0.11.0
Release:        1%{?dist}
Summary:        Deprecated misc library functions for OCaml
License:        LGPL
URL:            https://github.com/xapi-project/stdext
Source0:        https://github.com/xapi-project/stdext/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-uuidm-devel

%description
Deprecated misc library functions for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-fd-send-recv-devel%{?_isa}
BuildRequires:  ocaml-uuidm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n stdext-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%files
%doc README.md
%{_libdir}/ocaml/stdext
%exclude %{_libdir}/ocaml/stdext/*.a
%exclude %{_libdir}/ocaml/stdext/*.cmxa
%exclude %{_libdir}/ocaml/stdext/*.cmx
%exclude %{_libdir}/ocaml/stdext/*.mli
%{_libdir}/ocaml/stublibs/dllstdext_stubs.so
%{_libdir}/ocaml/stublibs/dllstdext_stubs.so.owner

%files devel
%{_libdir}/ocaml/stdext/*.a
%{_libdir}/ocaml/stdext/*.cmx
%{_libdir}/ocaml/stdext/*.cmxa
%{_libdir}/ocaml/stdext/*.mli

%changelog
* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.11.0-1
- Update to 0.11.0

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.10.0-2
- Split files correctly between base and devel packages

* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 0.10.0-1
- Update to 0.10.0, removing the Tar module (use ocaml-tar instead)

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

