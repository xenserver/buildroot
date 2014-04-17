Name:           ocaml-cmdliner
Version:        0.9.3
Release:        3%{?dist}
Summary:        Declarative definition of commandline interfaces for OCaml
License:        BSD3
URL:            http://erratique.ch/software/cmdliner
Source0:        https://github.com/dbuenzli/cmdliner/archive/v%{version}/cmdliner-%{version}.tar.gz
BuildRequires:  oasis
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
Obsoletes:      cmdliner <= 0.9.3

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
oasis setup
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install


%files
%doc CHANGES
%doc README
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
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Switch to GitHub mirror

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

