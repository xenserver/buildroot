Name:           ocaml-ipaddr
Version:        2.5.0
Release:        1000%{?dist}
Summary:        Pure OCaml parsers and printers for IP addresses
License:        ISC
URL:            https://github.com/mirage/ocaml-ipaddr
Source0:        https://github.com/mirage/ocaml-ipaddr/archive/%{version}/ocaml-ipaddr-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-camlp4

%description
A library for manipulation of IP (and MAC) address representations

%package        devel
Summary:        Development files for %{name}
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
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/ipaddr
%exclude %{_libdir}/ocaml/ipaddr/*.a
%exclude %{_libdir}/ocaml/ipaddr/*.cmxa
%exclude %{_libdir}/ocaml/ipaddr/*.cmx
%exclude %{_libdir}/ocaml/ipaddr/*.ml
%exclude %{_libdir}/ocaml/ipaddr/*.mli

%files devel
%{_libdir}/ocaml/ipaddr/*.a
%{_libdir}/ocaml/ipaddr/*.cmx
%{_libdir}/ocaml/ipaddr/*.cmxa
%{_libdir}/ocaml/ipaddr/*.mli

%changelog
* Sat Jul 19 2014 David Scott <dave.scott@citrix.com> - 2.5.0-1000
- Update to 2.5.0; override upstream package

* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 2.4.0-1
- Initial package

