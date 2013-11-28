Name:           xmlm
Version:        1.1.1
Release:        1
Summary:        Streaming XML input/output for OCaml
License:        BSD3
Group:          Development/Libraries
URL:            http://erratique.ch/software/xmlm
Source0:        http://erratique.ch/software/%{name}/releases/%{name}-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc
Requires:       ocaml ocaml-findlib

%description
Xmlm is an OCaml module providing streaming XML input/output. It aims at
making XML processing robust and painless.

The streaming interface can process documents without building an in-memory
representation. It lets the programmer translate its data structures to
XML documents and vice-versa. Functions are provided to easily transform
arborescent data structures to/from XML documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/xmltrip

%clean
rm -rf %{buildroot}

%files
#This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc README CHANGES
%{_libdir}/ocaml/xmlm/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.1.1-1
- Initial package

