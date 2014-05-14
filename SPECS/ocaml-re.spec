%global debug_package %{nil}

Name:           ocaml-re
Version:        1.2.2
Release:        2%{?dist}
Summary:        A regular expression library for OCaml
License:        LGPL
Group:          Development/Libraries
URL:            http://github.com/ocaml/ocaml-re
Source0:        http://github.com/ocaml/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
A regular expression library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
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
%doc LICENSE README.md CHANGES
%{_libdir}/ocaml/re/*

%changelog
* Wed May 14 2014 David Scott <dave.scott@citrix.com> - 1.2.2-2
- README has become README.md

* Mon May 12 2014 David Scott <dave.scott@eu.citrix.com> - 1.2.2-1
- Update to 1.2.2

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.1-1
- Initial package

