Name:           optcomp
Version:        1.4
Release:        1
Summary:        Optional compilation with cpp-like directives
License:        BSD3
Group:          Development/Other
URL:            http://forge.ocamlcore.org/projects/optcomp/
Source0:        https://forge.ocamlcore.org/frs/download.php/1011/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc ocaml-camlp4 ocaml-camlp4-devel
Requires:       ocaml

%description
Optional compilation with cpp-like directives.

%prep
%setup -q

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{_libdir}/ocaml/usr/local/bin/optcomp-r %{buildroot}/%{_bindir}/
mv %{buildroot}/%{_libdir}/ocaml/usr/local/bin/optcomp-o %{buildroot}/%{_bindir}/


%files
%defattr(-,root,root)
%doc LICENSE README
%{_libdir}/ocaml/optcomp/*
%{_bindir}/optcomp-r
%{_bindir}/optcomp-o

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.4-1
- Initial package

