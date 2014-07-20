%define debug_package %{nil}

Name:           ocamlscript
Version:        2.0.3
Release:        1%{?dist}
Summary:        OCamlscript is a tool which compiles OCaml scripts into native code, thus combining mthe flexibility of scripts and the speed provided by ocamlopt.
License:        Boost
URL:            http://mjambon.com/ocamlscript.html
Source0:        https://github.com/mjambon/ocamlscript/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib

%description
OCamlscript is a tool which compiles OCaml scripts into native code, thus combining mthe flexibility of scripts and the speed provided by ocamlopt.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ocamlscript %{buildroot}%{_bindir}/ocamlscript

export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=ignore
ocamlfind install ocamlscript META ocamlscript.cmi ocamlscript.cmo ocamlscript.cmx ocamlscript.o

%files
%doc Changes
%doc README.md
%{_bindir}/ocamlscript
%{_libdir}/ocaml/ocamlscript
%{_libdir}/ocaml/ocamlscript/META
%{_libdir}/ocaml/ocamlscript/ocamlscript.cmi
%{_libdir}/ocaml/ocamlscript/ocamlscript.cmo
%{_libdir}/ocaml/ocamlscript/ocamlscript.cmx
%{_libdir}/ocaml/ocamlscript/ocamlscript.o

%changelog
* Sun Jul 20 2014 David Scott <dave.scott@citrix.com> - 2.0.3-1
- Initial package
