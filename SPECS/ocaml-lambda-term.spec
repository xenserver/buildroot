%global debug_package %{nil}

Name:           ocaml-lambda-term
Version:        1.2
Release:        1%{?dist}
Summary:        Lambda-Term is a cross-platform library for manipulating the terminal for Ocaml
License:        BSD3
Group:          Development/Libraries
URL:            http://forge.ocamlcore.org/projects/lambda-term/
Source0:        http://forge.ocamlcore.org/frs/download.php/945/lambda-term-%{version}.tar.gz
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
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n lambda-term-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs

export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install

rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/lambda-term-actions

%files
# This space intentionally left blank

%files devel
%doc LICENSE CHANGES
%{_libdir}/ocaml/lambda-term/*
%{_libdir}/ocaml/stublibs/dlllambda-term_stubs.so
%{_libdir}/ocaml/stublibs/dlllambda-term_stubs.so.owner

%changelog
* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com> - 1.2-1
- Initial package

