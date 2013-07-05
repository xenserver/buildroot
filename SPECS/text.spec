%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-text
Version:        0.6
Release:        0%{?dist}
Summary:        OCaml-Text is a library for dealing with ``text'', i.e. sequence of unicode characters, in a convenient way.

Group:          Development/Libraries
License:        BSD
URL:            http://forge.ocamlcore.org/projects/ocaml-text
Source0:        http://forge.ocamlcore.org/frs/download.php/937/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-ocamldoc

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ocaml-text-%{version}
ocaml setup.ml -configure --destdir $RPM_BUILD_ROOT --prefix /usr

%build
ocaml setup.ml -build
ocaml setup.ml -doc

%install
rm -rf $RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install

# Remove this, reinstall it properly with a %%doc rule below.
rm -rf $RPM_BUILD_ROOT/usr/local/share/doc

%clean
rm -rf $RPM_BUILD_ROOT


%files devel
%defattr(-,root,root,-)
%doc /usr/share/doc/ocaml-text/*
%{_libdir}/ocaml/text/*
%{_libdir}/ocaml/stublibs/*
%changelog
