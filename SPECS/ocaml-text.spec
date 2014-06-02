%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-text
Version:        0.6
Release:        2%{?dist}
Summary:        Library for dealing with unicode text conveniently

License:        BSD
URL:            http://forge.ocamlcore.org/projects/ocaml-text
Source0:        http://forge.ocamlcore.org/frs/download.php/937/%{name}-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-ocamldoc

%description
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure --destdir $RPM_BUILD_ROOT --prefix /usr
make
make doc

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

# Remove this, reinstall it properly with a %%doc rule below.
rm -rf $RPM_BUILD_ROOT/usr/local/share/doc

%files
%{_libdir}/ocaml/text
%exclude %{_libdir}/ocaml/text/*.a
%exclude %{_libdir}/ocaml/text/*.cmxa
%exclude %{_libdir}/ocaml/text/*.cmx
%exclude %{_libdir}/ocaml/text/*.mli
%{_libdir}/ocaml/stublibs/dlltext-bigarray_stubs.so
%{_libdir}/ocaml/stublibs/dlltext-bigarray_stubs.so.owner
%{_libdir}/ocaml/stublibs/dlltext_stubs.so
%{_libdir}/ocaml/stublibs/dlltext_stubs.so.owner

%files devel
%doc /usr/share/doc/ocaml-text
%{_libdir}/ocaml/text/*.a
%{_libdir}/ocaml/text/*.cmx
%{_libdir}/ocaml/text/*.cmxa
%{_libdir}/ocaml/text/*.mli

%changelog
* Mon Jun 02 2014 Euan Harris <euan.harris@citrix.com> - 0.6-2
- Split files correctly between base and devel packages

* Sat Jun 01 2013 David Scott <dave.scott@eu.citrix.com> - 0.6-1
- Initial package

