Name:           ocaml-uri
Version:        1.3.8
Release:        0
Summary:        A URI library for OCaml
License:        ISC
Group:          Development/Other
URL:            https://github.com/mirage/ocaml-uri/archive/ocaml-uri-1.3.8.tar.gz
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc ocaml-re-devel
Requires:       ocaml ocaml-findlib

%description
A URI library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-uri-ocaml-uri-%{version}

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

%files devel
%defattr(-,root,root)
%doc README.md CHANGES
%{_libdir}/ocaml/uri/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

