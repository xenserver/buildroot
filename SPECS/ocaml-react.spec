%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-react
Version:        1.1.0
Release:        2%{?dist}
Summary:        OCaml framework for Functional Reactive Programming (FRP)


Group:          Development/Libraries
License:        BSD
URL:            http://erratique.ch/software/react

Source0:        http://erratique.ch/software/react/releases/react-%{version}.tbz
Source1:        react-LICENSE

BuildRequires:  ocaml >= 3.11.0
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
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n react-%{version}
cp %{SOURCE1} LICENSE

%build
ocaml pkg/build.ml native=true native-dynlink=true

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml/react
cp _build/pkg/META _build/src/react.a _build/src/react.cma _build/src/react.cmi _build/src/react.cmx _build/src/react.cmxa _build/src/react.cmxs _build/src/react.mli %{buildroot}/%{_libdir}/ocaml/react

%files
# This space intentionally left blank

%files devel
%doc CHANGES.md README.md
%{_libdir}/ocaml/react/*


%changelog
* Sun May 11 2014 David Scott <dave.scott@citrix.com> - 1.1.0-2
- Update for 1.1.0

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
