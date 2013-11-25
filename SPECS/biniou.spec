%define debug_package %{nil}

Name:           biniou
Version:        1.0.6
Release:        1
Summary:        Compact, fast and extensible serialization format
License:        BSD3
Group:          Development/Libraries
URL:            http://mjambon.com/biniou.html
Source0:        http://mjambon.com/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib easy-format
Requires:       ocaml ocaml-findlib

%description
Binary data format designed for speed, safety, ease of use and backward
compatibility as protocols evolve.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_libdir}/ocaml/biniou/*
%{_bindir}/bdump

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

