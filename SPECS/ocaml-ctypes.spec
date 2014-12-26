Name:           ocaml-ctypes
Version:        0.3.4
Release:        1%{?dist}
Summary:        Library for binding to C libraries using pure OCaml
License:        MIT
URL:            https://github.com/ocamllabs/ocaml-ctypes/
Source0:        https://github.com/ocamllabs/%{name}/archive/%{version}.tar.gz
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
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%files
%doc README.md LICENSE CHANGES.md
%{_libdir}/ocaml/ctypes
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
* Fri Dec 26 2014 David Scott <dave.scott@citrix.com>
- Update to 0.3.4

* Thu Apr 24 2014 David Scott <dave.scott@citrix.com>
- Fix the split between devel and main package, hopefully

* Wed Nov 13 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package

