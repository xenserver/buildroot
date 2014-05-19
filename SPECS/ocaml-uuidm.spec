%global debug_package %{nil}

Name:           ocaml-uuidm
Version:        0.9.5
Release:        2%{?dist}
Summary:        Universally Unique IDentifiers (UUIDs) for OCaml
License:        BSD3
Group:          Development/Libraries
URL:            http://erratique.ch/software/uuidm
Source0:        https://github.com/dbuenzli/uuidm/archive/v%{version}/uuidm-%{version}.tar.gz
BuildRequires:  oasis
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
Uuidm is an OCaml module implementing 128 bits universally unique
identifiers version 3, 5 (named based with MD5, SHA-1 hashing) and 4
(random based) according to RFC 4122.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uuidm-%{version}

%build
oasis setup
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/uuidtrip


%files
#This space intentionally left blank

%files devel
%doc README CHANGES
%{_libdir}/ocaml/uuidm/uuidm.mli
%{_libdir}/ocaml/uuidm/uuidm.cma
%{_libdir}/ocaml/uuidm/uuidm.cmxa
%{_libdir}/ocaml/uuidm/uuidm.a
%{_libdir}/ocaml/uuidm/uuidm.cmxs
%{_libdir}/ocaml/uuidm/uuidm.cmi
%{_libdir}/ocaml/uuidm/uuidm.cmx
%{_libdir}/ocaml/uuidm/META

%changelog
* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.5-2
- Switch to GitHub mirror

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.5-1
- Initial package

