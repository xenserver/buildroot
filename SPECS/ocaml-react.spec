%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-react
Version:        0.9.4
Release:        3%{?dist}
Summary:        OCaml framework for Functional Reactive Programming (FRP)
License:        BSD
URL:            http://erratique.ch/software/react
Source0:        https://github.com/dbuenzli/react/archive/v%{version}/react-%{version}.tar.gz
Source1:        react-LICENSE

BuildRequires:  oasis
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
React is an OCaml module for functional reactive programming (FRP). It
provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or
signal, this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n react-%{version}
cp %{SOURCE1} LICENSE

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
%{_libdir}/ocaml/react
%exclude %{_libdir}/ocaml/react/*.a
%exclude %{_libdir}/ocaml/react/*.cmxa
%exclude %{_libdir}/ocaml/react/*.cmx
%exclude %{_libdir}/ocaml/react/*.mli

%files devel
%{_libdir}/ocaml/react/*.a
%{_libdir}/ocaml/react/*.cmx
%{_libdir}/ocaml/react/*.cmxa
%{_libdir}/ocaml/react/*.mli

%changelog
* Thu May 29 2014 Euan Harris <euan.harris@citrix.com> - 0.9.4-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.4-2
- Switch to GitHub mirror

* Sat Jun 01 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update for 0.9.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 0.9.2-1
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-3
- Rebuild for OCaml 3.11.2.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-2
- Initial RPM release.
- Use global instead of define (Till Maas).
