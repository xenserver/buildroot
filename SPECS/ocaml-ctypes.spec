Name:           ocaml-ctypes
Version:        0.2.2
Release:        1%{?dist}
Summary:        Library for binding to C libraries using pure OCaml
License:        MIT
Group:          Development/Other
URL:            https://github.com/ocamllabs/ocaml-ctypes/
Source0:        https://github.com/ocamllabs/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         ocaml-ctypes-0.2.1-std-gnu99.patch
BuildRoot:      %{_tmppath}/%{name}-%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib libffi-devel
Requires:       ocaml ocaml-findlib

%description
Library for binding to C libraries using pure OCaml

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

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

%clean
rm -rf %{buildroot}

%files
%doc README.md LICENSE CHANGES
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
* Thu Apr 24 2014 David Scott <dave.scott@citrix.com>
- Fix the split between devel and main package, hopefully

* Wed Nov 13 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package

