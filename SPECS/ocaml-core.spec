%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-core
Version:        111.28.00
Release:        1%{?dist}
Summary:        System-independent part of Jane Street's Core.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/core_kernel
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/core-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-bin-prot-devel
BuildRequires:  ocaml-comparelib-devel
BuildRequires:  ocaml-fieldslib-devel
BuildRequires:  ocaml-herelib-devel
BuildRequires:  ocaml-pa-bench-devel
BuildRequires:  ocaml-pa-ounit-devel
BuildRequires:  ocaml-pa-pipebang-devel
BuildRequires:  ocaml-pa-test-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-typerep-devel
BuildRequires:  ocaml-variantslib-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-core-kernel-devel
BuildRequires:  ocaml-res-devel
BuildRequires:  chrpath

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Core is an industrial-strength alternative to the OCaml standard
library.  It was developed by Jane Street, which is the largest
industrial user of OCaml. Core_kernel is the system-independent
part of Core.  It is aimed for cases when the full Core is not
available, such as in Javascript.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n core-%{version}
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

strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYRIGHT.txt LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt MLton-license.txt
%{_libdir}/ocaml/core
%if %opt
%exclude %{_libdir}/ocaml/core/*.a
%exclude %{_libdir}/ocaml/core/*.cmxa
%endif
%exclude %{_libdir}/ocaml/core/*.ml
%exclude %{_libdir}/ocaml/core/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%defattr(-,root,root,-)
%doc COPYRIGHT.txt LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt README.md MLton-license.txt
%if %opt
%{_libdir}/ocaml/core/*.a
%{_libdir}/ocaml/core/*.cmxa
%endif
%{_libdir}/ocaml/core/*.ml
%{_libdir}/ocaml/core/*.mli

%changelog
* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 111.28.00-1
- Update to 111.28.00

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.55.02-1
- Initial package for Fedora 20.
