Name:           ocaml-cow
Version:        1.0.0
Release:        1%{?dist}
Summary:        XML, JSON, HTML, CSS, and Markdown syntax and libraries
License:        ISC
URL:            https://github.com/mirage/ocaml-cow
Source0:        https://github.com/mirage/ocaml-cow/archive/v1.0.0/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-type-conv
BuildRequires:  ocaml-ulex-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-uri-devel
BuildRequires:  ocaml-xmlm-devel
BuildRequires:  ocaml-omd-devel
BuildRequires:  ocaml-ezjsonm-devel
BuildRequires:  ocaml-dyntype-devel

%description

Writing web-applications requires a lot of skills: HTML, CSS, XML,
JSON and Markdown, to name but a few! This library provides OCaml
syntax extensions for these web formats by:

* extending standard OCaml syntax with embedded web DSLs. It has a
  quotation mechanism which parses HTML, CSS or XML to OCaml, and
  also anti-quotations that form a template mechanism.

* using type-driven code generation to generate markup directly from
  OCaml type declarations. It is possible to mix hand-written and
  generated code to deal with special-cases. Most of the work is done
  at pre-processing time, so there is no runtime costs and the generated
  OCaml code can be manually inspected if desired.

Mre documentation at <https://github.com/mirage/ocaml-cow>

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-findlib
Requires:       ocaml-ocamldoc
Requires:       ocaml-type-conv
Requires:       ocaml-ulex-devel
Requires:       ocaml-re-devel
Requires:       ocaml-ounit-devel
Requires:       ocaml-uri-devel
Requires:       ocaml-xmlm-devel
Requires:       ocaml-omd-devel
Requires:       ocaml-ezjsonm-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
make all

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%{_libdir}/ocaml/cow
%exclude %{_libdir}/ocaml/cow/*.a
%exclude %{_libdir}/ocaml/cow/*.cmxa
%exclude %{_libdir}/ocaml/cow/*.mli

%files devel
%{_libdir}/ocaml/cow/*.a
%{_libdir}/ocaml/cow/*.cmxa
%{_libdir}/ocaml/cow/*.mli

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
