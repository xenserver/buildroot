Name:           cppo
Version:        0.9.3
Release:        2%{?dist}
Summary:        Equivalent of the C preprocessor for OCaml
License:        BSD3
URL:            http://mjambon.com/cppo.html
Source0:        https://github.com/mjambon/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml

%description
Equivalent of the C preprocessor for OCaml.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}

%files
%doc LICENSE 
%doc README
%{_bindir}/cppo

%changelog
* Tue Oct 21 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Switch to GitHub sources

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

