%global debug_package %{nil}

Name:           ocaml-obuild
Version:        0.0.2
Release:        1%{?dist}
Summary:        Simple build tool for OCaml programs
License:        BSD2
URL:            http://github.com/vincenthz/obuild
Source0:        https://github.com/vincenthz/obuild/archive/v%{version}/obuild-%{version}.tar.gz
BuildRequires:  ocaml

%description
The goal is to make a very simple build system for users and developers 
of OCaml libraries and programs.

Obuild acts as a building black box: user declares only what they want to 
build and with which sources, and the build system will consistently 
build it.

The design is based on cabal, and borrows most of its layout and way of 
working, adapting parts where necessary to support OCaml fully.

%prep
%setup -q -n obuild-%{version}

%build
./bootstrap

%install
mkdir -p %{buildroot}/%{_bindir}
install dist/build/obuild/obuild %{buildroot}/%{_bindir}
install dist/build/obuild-simple/obuild-simple %{buildroot}/%{_bindir}
install dist/build/obuild-from-oasis/obuild-from-oasis %{buildroot}/%{_bindir}


%files
%doc README.md TODO.md DESIGN.md LICENSE OBUILD_SPEC.md
%{_bindir}/obuild
%{_bindir}/obuild-simple
%{_bindir}/obuild-from-oasis

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.0.2-1
- Initial package

