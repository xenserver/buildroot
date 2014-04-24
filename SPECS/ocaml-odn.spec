Name:		ocaml-odn
Version:	0.0.11
Release:	1%{?dist}
Summary:	Dump OCaml data structures using OCaml data notation

Group:		Development/Libraries
License:	LGPL
URL:		https://forge.ocamlcore.org/projects/odn/
Source0:	https://forge.ocamlcore.org/frs/download.php/1310/ocaml-data-notation-%{version}.tar.gz

BuildRequires:	ocaml >= 3.10.2
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-type-conv >= 108.07.01
BuildRequires:	ocaml-ounit-devel >= 2.0.0
BuildRequires:	ocaml-fileutils-devel >= 0.4.0

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ocaml-data-notation-%{version}


%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install


%files
%doc COPYING.txt CHANGES.txt
%{_libdir}/ocaml/odn/META
%{_libdir}/ocaml/odn/*.cma
%{_libdir}/ocaml/odn/*.cmi


%files devel
%{_libdir}/ocaml/odn/*.a
%{_libdir}/ocaml/odn/*.cmx
%{_libdir}/ocaml/odn/*.cmxa
%exclude %{_libdir}/ocaml/odn/*.cmxs
%exclude %{_libdir}/ocaml/odn/*.ml

%changelog
* Tue Mar 25 2014 Euan Harris <euan.harris@citrix.com> - 0.0.11-1
- Initial package

