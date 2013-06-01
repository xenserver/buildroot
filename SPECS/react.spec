%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-react
Version:        0.9.4
Release:        0%{?dist}
Summary:        OCaml framework for Functional Reactive Programming (FRP)

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Group:          Development/Libraries
License:        BSD
URL:            http://erratique.ch/software/react

Source0:        http://erratique.ch/software/react/releases/react-%{version}.tbz
Source1:        react-LICENSE

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel

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
chmod +x build


%build
./build


%install
rm -rf $RPM_BUILD_ROOT
export INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/react
mkdir -p $INSTALLDIR
./build install


%check
%if %opt
./build test.native
./_build/test/test.native
./build clock.native
#./_build/test/clock.native
./build breakout.native
#./_build/test/breakout.native
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/ocaml/react
%if %opt
%exclude %{_libdir}/ocaml/react/*.cmx
%endif
%exclude %{_libdir}/ocaml/react/*.mli
%exclude %{_libdir}/ocaml/react/*.ml


%files devel
%defattr(-,root,root,-)
%doc CHANGES README
%if %opt
%{_libdir}/ocaml/react/*.cmx
%endif
%{_libdir}/ocaml/react/*.mli
%{_libdir}/ocaml/react/*.ml


%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 0.9.2-1
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-3
- Rebuild for OCaml 3.11.2.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-2
- Initial RPM release.
- Use global instead of define (Till Maas).
