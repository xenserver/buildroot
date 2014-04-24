%global debug_package %{nil}

Name:           ocaml-cstruct
Version:        0.7.1
Release:        2%{?dist}
Summary:        Read and write low-level C-style structures in OCaml
License:        ISC
Group:          Development/Libraries
URL:            https://github.com/mirage/ocaml-cstruct
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocplib-endian-devel

%description
Read and write low-level C-style structures in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-ocplib-endian-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml --enable-lwt
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs

export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install DESTDIR=%{buildroot}


%files
# This space intentionally left blank

%files devel
%doc README.md CHANGES
%{_libdir}/ocaml/cstruct/*
%{_libdir}/ocaml/stublibs/dllcstruct_stubs.so
%{_libdir}/ocaml/stublibs/dllcstruct_stubs.so.owner

%changelog
* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.7.1-2
- Add dependency on lwt so the cstruct.lwt package is built

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

