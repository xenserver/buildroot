Name:           ocaml-xmlm
Version:        1.2.0
Release:        1%{?dist}
Summary:        Streaming XML input/output for OCaml
License:        BSD3
URL:            http://erratique.ch/software/xmlm
Source0:        https://github.com/dbuenzli/xmlm/archive/v%{version}/xmlm-%{version}.tar.gz
Obsoletes:      xmlm <= 1.1.1
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
Xmlm is an OCaml module providing streaming XML input/output. It aims at
making XML processing robust and painless.

The streaming interface can process documents without building an in-memory
representation. It lets the programmer translate its data structures to
XML documents and vice-versa. Functions are provided to easily transform
arborescent data structures to/from XML documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xmlm-%{version}

%build
./pkg/pkg-git
./pkg/build true

%install
find .
mkdir -p %{buildroot}/%{_libdir}/ocaml/xmlm
cp _build/pkg/META  _build/src/xmlm.a  _build/src/xmlm.cma  _build/src/xmlm.cmi  _build/src/xmlm.cmx  _build/src/xmlm.cmxa  _build/src/xmlm.cmxs  _build/src/xmlm.mli  %{buildroot}/%{_libdir}/ocaml/xmlm



%files
%doc CHANGES
%doc README
%{_libdir}/ocaml/xmlm
%exclude %{_libdir}/ocaml/xmlm/*.a
%exclude %{_libdir}/ocaml/xmlm/*.cmxa
%exclude %{_libdir}/ocaml/xmlm/*.cmx
%exclude %{_libdir}/ocaml/xmlm/*.mli

%files devel
%{_libdir}/ocaml/xmlm/*.a
%{_libdir}/ocaml/xmlm/*.cmxa
%{_libdir}/ocaml/xmlm/*.cmx
%{_libdir}/ocaml/xmlm/*.mli

%changelog
* Thu Jul 17 2014 David Scott <dave.scott@citri.com> - 1.2.0-1
- Update to 1.2.0

* Mon Jun 2 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-2
- Switch to GitHub mirror

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.1.1-1
- Initial package

