%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-core-bench
Version:        109.58.00
Release:        1%{?dist}
Summary:        System-independent part of Jane Street's Core.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/core_bench
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/core_bench-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-core-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-fieldslib-devel
BuildRequires:  ocaml-comparelib-devel
BuildRequires:  ocaml-textutils-devel
BuildRequires:  ocaml-pa-ounit-devel
BuildRequires:  ocaml-core-extended-devel
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
%setup -q -n core_bench-%{version}
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
%doc README.md
%{_libdir}/ocaml/core_bench
%if %opt
%exclude %{_libdir}/ocaml/core_bench/*.a
%exclude %{_libdir}/ocaml/core_bench/*.cmxa
%endif
%exclude %{_libdir}/ocaml/core_bench/*.ml
%exclude %{_libdir}/ocaml/core_bench/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%defattr(-,root,root,-)
%doc README.md
%if %opt
%{_libdir}/ocaml/core_bench/*.a
%{_libdir}/ocaml/core_bench/*.cmxa
%endif
%{_libdir}/ocaml/core_bench/*.ml
%{_libdir}/ocaml/core_bench/*.mli

%changelog
* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 109.58.00-1
- Update to 109.58.00

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.55.02-1
- Initial package for Fedora 20.
