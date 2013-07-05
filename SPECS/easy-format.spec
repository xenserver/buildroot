Name:           easy-format
Version:        1.0.1
Release:        0
Summary:        Indentation made easy
License:        BSD3
Group:          Development/Other
URL:            http://mjambon.com/releases/easy-format/easy-format-1.0.1.tar.gz
Source0:        http://mjambon.com/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Easy_format: indentation made easy.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_libdir}/ocaml/easy-format/*

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

