Name:		ocaml-odn
Version:	0.0.11
Release:	1%{?dist}
Summary:	Dump OCaml data structures using OCaml data notation

License:	LGPL
URL:		https://forge.ocamlcore.org/projects/odn/
Source0:	https://forge.ocamlcore.org/frs/download.php/1310/ocaml-data-notation-%{version}.tar.gz

BuildRequires:	ocaml >= 3.10.2
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-type-conv >= 108.07.01
BuildRequires:	ocaml-ounit-devel >= 2.0.0
BuildRequires:	ocaml-fileutils-devel >= 0.4.0

%description
This library uses type-conv to dump OCaml data structure using OCaml data
notation. This kind of data dumping helps to write OCaml code generator,
like OASIS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:	ocaml-type-conv%{_isa} >= 108.07.01

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-data-notation-%{version}

%build
./configure --destdir %{buildroot}/%{_libdir}/ocaml
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES.txt
%doc COPYING.txt
%{_libdir}/ocaml/odn
%exclude %{_libdir}/ocaml/odn/*.a
%exclude %{_libdir}/ocaml/odn/*.cmxa
%exclude %{_libdir}/ocaml/odn/*.cmx

%files devel
%{_libdir}/ocaml/odn/*.a
%{_libdir}/ocaml/odn/*.cmx
%{_libdir}/ocaml/odn/*.cmxa

%changelog
* Tue Mar 25 2014 Euan Harris <euan.harris@citrix.com> - 0.0.11-1
- Initial package

