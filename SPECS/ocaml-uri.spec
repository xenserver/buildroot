Name:           ocaml-uri
Version:        1.3.8
Release:        3%{?dist}
Summary:        A URI library for OCaml
License:        ISC
Group:          Development/Libraries
URL:            https://github.com/mirage/ocaml-uri
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml >= 4.00
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-re-devel

%description
A URI library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/uri
%exclude %{_libdir}/ocaml/uri/*.a
%exclude %{_libdir}/ocaml/uri/*.cmxa
%exclude %{_libdir}/ocaml/uri/*.cmx
%exclude %{_libdir}/ocaml/uri/*.ml
%exclude %{_libdir}/ocaml/uri/*.mli

%files devel
%{_libdir}/ocaml/uri/*.a
%{_libdir}/ocaml/uri/*.cmx
%{_libdir}/ocaml/uri/*.cmxa
%{_libdir}/ocaml/uri/*.mli

%changelog
* Sun May 11 2014 David Scott <dave.scott@citrix.com> - 1.3.8-3
- Distribute files between %{name} and %{name}-devel

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.3.8-1
- Initial package

