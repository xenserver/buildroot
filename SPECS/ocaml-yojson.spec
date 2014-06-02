%global debug_package %{nil}

Name:           ocaml-yojson
Version:        1.1.6
Release:        2%{?dist}
Summary:        A JSON parser and printer for OCaml
License:        BSD3
URL:            http://mjambon.com/yojson.html
Source0:        http://mjambon.com/releases/yojson/yojson-%{version}.tar.gz
BuildRequires:  cppo
BuildRequires:  ocaml
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-findlib

%description
A JSON parser and printer for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-biniou-devel%{?_isa}
Requires:       ocaml-easy-format-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n yojson-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p %{buildroot}/%{_bindir}
make install DESTDIR=%{buildroot} BINDIR=%{buildroot}/%{_bindir}

%files
%doc README.md
%doc LICENSE
%{_bindir}/ydump
%{_libdir}/ocaml/yojson
%exclude %{_libdir}/ocaml/yojson/*.cmx
%exclude %{_libdir}/ocaml/yojson/*.mli

%files devel
%{_libdir}/ocaml/yojson/*.cmx
%{_libdir}/ocaml/yojson/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.1.6-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.1.6-1
- Initial package

