Name:           cppo
Version:        0.9.3
Release:        1
Summary:        Equivalent of the C preprocessor for OCaml
License:        BSD3
Group:          Development/Other
URL:            http://mjambon.com/cppo.html
Source0:        http://mjambon.com/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
Requires:       ocaml

%description
Equivalent of the C preprocessor for OCaml.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/cppo

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

