%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-typerep
Version:        109.55.02
Release:        1%{?dist}
Summary:        Runtime types for OCaml.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/typerep
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/typerep-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-bin-prot >= 109.53.02
BuildRequires:  ocaml-sexplib >= 109.55.02

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Runtime types for OCaml.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n typerep-%{version}
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir} \
      --destdir $RPM_BUILD_ROOT

%build
ocaml setup.ml -build


%check
ocaml setup.ml -test


%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%{_libdir}/ocaml/
%if %opt
%exclude %{_libdir}/ocaml/typerep_kernel/*.a
%exclude %{_libdir}/ocaml/typerep_kernel/*.cmxa
%exclude %{_libdir}/ocaml/typerep_core/*.a
%exclude %{_libdir}/ocaml/typerep_core/*.cmxa
%exclude %{_libdir}/ocaml/typerep_kernel/*.a
%exclude %{_libdir}/ocaml/typerep_generics_sexprep/*.cmxa
%endif
%exclude %{_libdir}/ocaml/typerep_kernel/*.ml
%exclude %{_libdir}/ocaml/typerep_kernel/*.mli
%exclude %{_libdir}/ocaml/typerep_core/*.ml
%exclude %{_libdir}/ocaml/typerep_core/*.mli
%exclude %{_libdir}/ocaml/typerep_kernel/*.ml
%exclude %{_libdir}/ocaml/typerep_generics_sexprep/*.mli


%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/typerep_kernel/*.a
%{_libdir}/ocaml/typerep_kernel/*.cmxa
%{_libdir}/ocaml/typerep_core/*.a
%{_libdir}/ocaml/typerep_core/*.cmxa
%{_libdir}/ocaml/typerep_kernel/*.a
%{_libdir}/ocaml/typerep_generics_sexprep/*.cmxa
%endif
%{_libdir}/ocaml/typerep_kernel/*.ml
%{_libdir}/ocaml/typerep_kernel/*.mli
%{_libdir}/ocaml/typerep_core/*.ml
%{_libdir}/ocaml/typerep_core/*.mli
%{_libdir}/ocaml/typerep_kernel/*.ml
%{_libdir}/ocaml/typerep_generics_sexprep/*.mli

%changelog
* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.55.02-1
- Initial package for Fedora 20.
