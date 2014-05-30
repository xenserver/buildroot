%global debug_package %{nil}

Name:           ocaml-re
Version:        1.2.1
Release:        1%{?dist}
Summary:        A regular expression library for OCaml
License:        LGPL
URL:            http://github.com/ocaml/ocaml-re
Source0:        http://github.com/ocaml/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
A regular expression library for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%doc LICENSE README CHANGES
%{_libdir}/ocaml/re/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.1-1
- Initial package

