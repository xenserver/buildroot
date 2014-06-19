%global debug_package %{nil}

Name:           ocaml-lambda-term
Version:        1.6
Release:        1%{?dist}
Summary:        Lambda-Term is a cross-platform library for manipulating the terminal for Ocaml
License:        BSD3
URL:            http://forge.ocamlcore.org/projects/lambda-term/
Source0:        https://github.com/diml/lambda-term/archive/%{version}/lambda-term-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-camomile-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-zed-devel

%description
Lambda-Term is a cross-platform library for manipulating the terminal.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n lambda-term-%{version}

%build
./configure --destdir %{buildroot}/%{_libdir}/ocaml
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install

rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/lambda-term-actions

%files
%doc CHANGES.md
%doc LICENSE
%{_libdir}/ocaml/lambda-term
%{_libdir}/ocaml/stublibs/dlllambda-term_stubs.so
%{_libdir}/ocaml/stublibs/dlllambda-term_stubs.so.owner
%exclude %{_libdir}/ocaml/lambda-term/*.a
%exclude %{_libdir}/ocaml/lambda-term/*.cmxa
%exclude %{_libdir}/ocaml/lambda-term/*.cmx
%exclude %{_libdir}/ocaml/lambda-term/*.mli

%files devel
%{_libdir}/ocaml/lambda-term/*.a
%{_libdir}/ocaml/lambda-term/*.cmx
%{_libdir}/ocaml/lambda-term/*.cmxa
%{_libdir}/ocaml/lambda-term/*.mli

%files devel
%{_libdir}/ocaml/lambda-term/*.a
%{_libdir}/ocaml/lambda-term/*.cmx
%{_libdir}/ocaml/lambda-term/*.cmxa
%{_libdir}/ocaml/lambda-term/*.mli

%changelog
* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 1.6-1
- Update to 1.6

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.2-2
- Split files correctly between base and devel packages

* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com> - 1.2-1
- Initial package

