%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-variantslib
Version:        109.15.02
Release:        1%{?dist}
Summary:        OCaml variants as first class values

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/variantslib
Source0:        https://ocaml.janestreet.com/ocaml-core/109.15.00/individual/variantslib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-type-conv >= 109.53.02
BuildRequires:  ocaml-ocamldoc

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
OCaml variants as first class values.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n variantslib-%{version}
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
%doc COPYRIGHT.txt LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%{_libdir}/ocaml/variantslib
%if %opt
%exclude %{_libdir}/ocaml/variantslib/*.a
%exclude %{_libdir}/ocaml/variantslib/*.cmxa
%endif
%exclude %{_libdir}/ocaml/variantslib/*.mli


%files devel
%defattr(-,root,root,-)
%doc COPYRIGHT.txt LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt README.txt
%if %opt
%{_libdir}/ocaml/variantslib/*.a
%{_libdir}/ocaml/variantslib/*.cmxa
%endif
%{_libdir}/ocaml/variantslib/*.mli


%changelog
* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.15.02-1
- Initial package for Fedora 20.
