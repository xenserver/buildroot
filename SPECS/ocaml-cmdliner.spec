Name:           ocaml-cmdliner
Version:        0.9.5
Release:        1%{?dist}
Summary:        Declarative definition of commandline interfaces for OCaml
License:        BSD3
URL:            http://erratique.ch/software/cmdliner
Source0:        http://erratique.ch/software/cmdliner/releases/cmdliner-%{version}.tbz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
Obsoletes:      cmdliner <= 0.9.5

%description
Cmdliner is an OCaml module for the declarative definition of command line
interfaces. It provides a simple and compositional mechanism to convert
command line arguments to OCaml values and pass them to your functions.
The module automatically handles syntax errors, help messages and UNIX
man page generation. It supports programs with single or multiple commands
(like darcs or git) and respects most of the POSIX and GNU conventions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cmdliner-%{version}

%build
ocaml pkg/git.ml
ocaml pkg/build.ml native=true native-dynlink=true

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml/cmdliner
find .
cp _build/src/cmdliner.a _build/src/cmdliner.cma _build/src/cmdliner.cmi _build/src/cmdliner.cmx _build/src/cmdliner.cmxa _build/src/cmdliner.cmxs _build/src/cmdliner.mli _build/pkg/META %{buildroot}/%{_libdir}/ocaml/cmdliner

%files
%doc CHANGES.md
%doc README.md
%{_libdir}/ocaml/cmdliner
%exclude %{_libdir}/ocaml/cmdliner/*.a
%exclude %{_libdir}/ocaml/cmdliner/*.cmxa
%exclude %{_libdir}/ocaml/cmdliner/*.cmx
%exclude %{_libdir}/ocaml/cmdliner/*.mli

%files devel
%{_libdir}/ocaml/cmdliner/*.a
%{_libdir}/ocaml/cmdliner/*.cmx
%{_libdir}/ocaml/cmdliner/*.cmxa
%{_libdir}/ocaml/cmdliner/*.mli

%changelog
* Thu Jul 17 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Switch to GitHub mirror

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

