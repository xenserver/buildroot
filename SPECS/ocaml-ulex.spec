Name:           ocaml-ulex
Version:        1.1
Release:        1%{?dist}
Summary:        lexer generator for Unicode and OCaml
License:        ISC
URL:            http://ftp.de.debian.org/debian/pool/main/u/ulex/ulex_1.1.orig.tar.gz
Source0:        http://ftp.de.debian.org/debian/pool/main/u/ulex/ulex_1.1.orig.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel

%description
lexer generator for Unicode and OCaml

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ulex-%{version}

%build
make
make all.opt

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%{_libdir}/ocaml/ulex
%exclude %{_libdir}/ocaml/ulex/*.a
%exclude %{_libdir}/ocaml/ulex/*.cmxa
%exclude %{_libdir}/ocaml/ulex/*.cmx
%exclude %{_libdir}/ocaml/ulex/*.mli

%files devel
%{_libdir}/ocaml/ulex/*.a
%{_libdir}/ocaml/ulex/*.cmxa
%{_libdir}/ocaml/ulex/*.cmx
%{_libdir}/ocaml/ulex/*.mli

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 1.1-1
- Initial package
