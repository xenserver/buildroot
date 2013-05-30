Name:           ocaml-obuild
Version:        0.0.2
Release:        0
Summary:        Simple build tool for OCaml programs
License:        BSD2
Group:          Development/Other
URL:            http://github.com/vincenthz/obuild
Source0:        obuild-0.0.2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
Requires:       ocaml

%description
The goal is to make a very simple build system for users and developers 
of OCaml library and programs.

Obuild acts as building black box: user declares only what they want to 
build and with which sources, and the build system will consistantly 
build it.

The design is based on cabal, and borrow most of the layout and way of 
working, adapting parts where necessary to support OCaml fully.

%prep
%setup -q -n obuild-%{version}

%build
./bootstrap

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install dist/build/obuild/obuild %{buildroot}/%{_bindir}
install dist/build/obuild-simple/obuild-simple %{buildroot}/%{_bindir}
install dist/build/obuild-from-oasis/obuild-from-oasis %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}
rm -rf dist

%files
%defattr(-,root,root)
%doc README.md TODO.md DESIGN.md LICENSE OBUILD_SPEC.md
%{_bindir}/obuild
%{_bindir}/obuild-simple
%{_bindir}/obuild-from-oasis

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

