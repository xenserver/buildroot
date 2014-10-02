Name:           optcomp
Version:        1.6
Release:        1%{?dist}
Summary:        Optional compilation with cpp-like directives
License:        BSD3
URL:            https://github.com/diml/optcomp
Source0:        https://github.com/diml/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

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
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/optcomp
%{_bindir}/optcomp-r
%{_bindir}/optcomp-o

%changelog
* Thu Oct 2 2014 Euan Harris <euan.harris@citrix.com> - 1.6-1
- Update to 1.6 and switch to GitHub sources

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.4-1
- Initial package

