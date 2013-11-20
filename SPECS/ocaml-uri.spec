%global debug_package %{nil}

Name:           ocaml-uri
Version:        1.3.8
Release:        1
Summary:        A URI library for OCaml
License:        ISC
Group:          Development/Other
URL:            https://github.com/mirage/ocaml-uri
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 4.00, ocaml-findlib, ocaml-ocamldoc, ocaml-re-devel, ocaml-compiler-libs
Requires:       ocaml, ocaml-findlib

%description
A URI library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
#This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc README.md CHANGES
%{_libdir}/ocaml/uri/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

