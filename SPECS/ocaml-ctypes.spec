Name:           ocaml-ctypes
Version:        0.4.1
Release:        2%{?dist}
Summary:        Library for binding to C libraries using pure OCaml
License:        MIT
URL:            https://github.com/ocamllabs/ocaml-ctypes/
Source0:        https://github.com/ocamllabs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib libffi-devel
Requires:       ocaml ocaml-findlib

%description
Library for binding to C libraries using pure OCaml

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README.md LICENSE CHANGES.md
%{_libdir}/ocaml/ctypes
%{_libdir}/ocaml/stublibs/dllctypes_stubs.so
%{_libdir}/ocaml/stublibs/dllctypes_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllctypes-foreign-base_stubs.so
%{_libdir}/ocaml/stublibs/dllctypes-foreign-base_stubs.so.owner
%exclude %{_libdir}/ocaml/ctypes/*.a
%exclude %{_libdir}/ocaml/ctypes/*.cmxa
%exclude %{_libdir}/ocaml/ctypes/*.cmx
%exclude %{_libdir}/ocaml/ctypes/*.mli

%files devel
%{_libdir}/ocaml/ctypes/*.a
%{_libdir}/ocaml/ctypes/*.cmx
%{_libdir}/ocaml/ctypes/*.cmxa
%{_libdir}/ocaml/ctypes/*.mli

%changelog
* Fri May  1 2015 Si Beaumont <simon.beaumont@citrix.com> - 0.4.1-2
- Package shared libaries in the right place

* Thu Apr 16 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.4.1-1
- New upstream release

* Thu Apr 24 2014 David Scott <dave.scott@citrix.com>
- Fix the split between devel and main package, hopefully

* Wed Nov 13 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package

