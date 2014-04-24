%global debug_package %{nil}

Name:           ocaml-ocplib-endian
Version:        0.4
Release:        1%{?dist}
Summary:        Optimized functions to read and write int16/32/64 from strings and bigarrays
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/OCamlPro/ocplib-endian
Source0:        https://github.com/OCamlPro/ocplib-endian/archive/%{version}/ocplib-endian-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  optcomp
Requires:       ocaml
Requires:       ocaml-findlib

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
Group:          Development/Libraries
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
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%doc COPYING.txt README.md
%{_libdir}/ocaml/ocplib-endian/*

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.4-1
- Initial package

