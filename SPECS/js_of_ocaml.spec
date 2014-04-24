%define debug_package %{nil}

Name:           js_of_ocaml
Version:        1.3.2
Release:        1%{?dist}
Summary:        Compile OCaml programs to javascript
License:        LGPL and others
Group:          Development/Other
URL:            http://ocsigen.org/download/js_of_ocaml-1.3.2.tar.gz
Source0:        http://ocsigen.org/download/%{name}-%{version}.tar.gz
BuildRequires:  deriving-ocsigen-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocamldoc
Requires:       deriving-ocsigen-devel
Requires:       ocaml
Requires:       ocaml-camlp4-devel
Requires:       ocaml-findlib
Requires:       ocaml-findlib-devel
Requires:       ocaml-lwt-devel

%description
Compile OCaml programs to Javascript.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}/


%files
# This space intentionally left blank

%files devel
%doc LICENSE README CHANGES
%{_libdir}/ocaml/js_of_ocaml/*
%{_libdir}/ocaml/stublibs/dlljs_of_ocaml.so
%{_libdir}/ocaml/stublibs/dlljs_of_ocaml.so.owner
%{_bindir}/js_of_ocaml

%changelog
* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com> - 1.3.2-1
- Initial package

