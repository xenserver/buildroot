%global debug_package %{nil}

Name:           ocaml-base64
Version:        2.0.0
Release:        1%{?dist}
Summary:        Base64 encoding and decoding library
License:        ISC
URL:            https://github.com/mirage/ocaml-base64
Source0:        https://github.com/mirage/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
Base64 is a group of similar binary-to-text encoding schemes that represent
binary data in an ASCII string format by translating it into a radix-64
representation.  It is specified in RFC 2045.

From version 2.0 upwards, the module name is called `B64` to avoid clashing
with other libraries such as `extlib` that use the `Base64` toplevel name.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q 

%build
# Dirty hack
export PREFIX=%{buildroot}%{_prefix}
ocaml setup.ml -configure --prefix prefix
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%files
%doc CHANGES.md
%doc README.md
%{_libdir}/ocaml/base64
%exclude %{_libdir}/ocaml/base64/*.a
%exclude %{_libdir}/ocaml/base64/*.cmxa
%exclude %{_libdir}/ocaml/base64/*.cmx
%exclude %{_libdir}/ocaml/base64/*.mli

%files devel
%{_libdir}/ocaml/base64/*.a
%{_libdir}/ocaml/base64/*.cmx
%{_libdir}/ocaml/base64/*.cmxa
%{_libdir}/ocaml/base64/*.mli

%changelog
* Thu Apr  2 2015 David Scott <dave.scott@citrix.com> - 2.0.0-1
- Initial package
