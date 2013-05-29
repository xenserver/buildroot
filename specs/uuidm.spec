Name:           ocaml-uuidm
Version:        0.9.5
Release:        0
Summary:        Universally Unique IDentifiers (UUIDs) for OCaml
License:        BSD3
Group:          Development/Other
URL:            http://erratique.ch/software/uuidm
Source0:        uuidm-0.9.5.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Uuidm is an OCaml module implementing 128 bits universally unique
identifiers version 3, 5 (named based with MD5, SHA-1 hashing) and 4
(random based) according to RFC 4122.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uuidm-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/uuidtrip

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
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
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

