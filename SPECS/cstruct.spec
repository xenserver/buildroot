Name:           ocaml-cstruct
Version:        0.7.1
Release:        0
Summary:        Read and write low-level C-style structures in OCaml
License:        ISC
Group:          Development/Other
URL:            https://github.com/mirage/ocaml-cstruct/archive/ocaml-cstruct-0.7.1.tar.gz
Source0:        ocaml-cstruct-0.7.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ocplib-endian-devel ocaml-camlp4 ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib

%description
Read and write low-level C-style structures in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-cstruct-ocaml-cstruct-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md CHANGES
%{_libdir}/ocaml/cstruct/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

