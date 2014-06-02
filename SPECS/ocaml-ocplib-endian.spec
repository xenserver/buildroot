%global debug_package %{nil}

Name:           ocaml-ocplib-endian
Version:        0.4
Release:        2%{?dist}
Summary:        Optimized functions to read and write int16/32/64 from strings and bigarrays
License:        LGPL
URL:            https://github.com/OCamlPro/ocplib-endian
Source0:        https://github.com/OCamlPro/ocplib-endian/archive/%{version}/ocplib-endian-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  optcomp

%description
Optimised functions to read and write int16/32/64 from strings and
bigarrays, based on new primitives added in version 4.01.

The library implements two modules:
- [EndianString](ocplib-endian/blob/master/src/endianString.mli) works
  directly on strings, and provides submodules BigEndian and LittleEndian,
  with their unsafe counter-parts;

- [EndianBigstring](ocplib-endian/blob/master/src/endianBigstring.mli)
  works on bigstrings (Bigarrays of chars), and provides submodules
  BigEndian and LittleEndian, with their unsafe counter-parts;


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       optcomp

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocplib-endian-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%files
%doc COPYING.txt
%doc README.md
%{_libdir}/ocaml/ocplib-endian
%exclude %{_libdir}/ocaml/ocplib-endian/*.a
%exclude %{_libdir}/ocaml/ocplib-endian/*.cmxa
%exclude %{_libdir}/ocaml/ocplib-endian/*.cmx
%exclude %{_libdir}/ocaml/ocplib-endian/*.mli

%files devel
%{_libdir}/ocaml/ocplib-endian/*.a
%{_libdir}/ocaml/ocplib-endian/*.cmx
%{_libdir}/ocaml/ocplib-endian/*.cmxa
%{_libdir}/ocaml/ocplib-endian/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.4-2
- Split files correctly between base and devel packages

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.4-1
- Initial package

