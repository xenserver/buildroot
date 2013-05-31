Name:           ocaml-ocplib-endian
Version:        0.3
Release:        0
Summary:        Optimised functions to read and write int16/32/64 from strings and bigarrays, based on new primitives added in version 4.01.
License:        LGPL
Group:          Development/Other
URL:            https://github.com/OCamlPro/ocplib-endian/archive/0.3.tar.gz
Source0:        ocplib-endian-0.3.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Optimised functions to read and write int16/32/64 from strings and
bigarrays, based on new primitives added in version 4.01.

The library implements two modules:
- [EndianString](ocplib-endian/blob/master/src/endianString.mli) works directly on strings, and provides submodules BigEndian and LittleEndian, with their unsafe counter-parts;
- [EndianBigstring](ocplib-endian/blob/master/src/endianBigstring.mli) works on bigstrings (Bigarrays of chars), and provides submodules BigEndian and LittleEndian, with their unsafe counter-parts;


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocplib-endian-%{version}

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
%doc COPYING.txt README.md
%{_libdir}/ocaml/ocplib-endian/*

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

