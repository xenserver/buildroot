%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-async-kernel
Version:        111.28.00
Release:        1%{?dist}
Summary:        Monad concurrency library

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/async_kernel
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/async_kernel-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-bin-prot-devel
BuildRequires:  ocaml-core-devel
BuildRequires:  ocaml-fieldslib-devel
BuildRequires:  ocaml-pa-ounit-devel
BuildRequires:  ocaml-pa-test-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-herelib-devel
BuildRequires:  ocaml-comparelib-devel
BuildRequires:  ocaml-enumerate-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Part of Jane Street’s Core library
The Core suite of libraries is an industrial strength alternative to
OCaml's standard library that was developed by Jane Street, the
largest industrial user of OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:  ocaml-bin-prot-devel
Requires:  ocaml-core-devel
Requires:  ocaml-fieldslib-devel
Requires:  ocaml-pa-ounit-devel
Requires:  ocaml-pa-test-devel
Requires:  ocaml-sexplib-devel
Requires:  ocaml-herelib-devel
Requires:  ocaml-comparelib-devel
Requires:  ocaml-enumerate-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n async_kernel-%{version}
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
%doc LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%{_libdir}/ocaml/async_kernel
%if %opt
%exclude %{_libdir}/ocaml/async_kernel/*.a
%exclude %{_libdir}/ocaml/async_kernel/*.cmxa
%endif
%exclude %{_libdir}/ocaml/async_kernel/*.ml
%exclude %{_libdir}/ocaml/async_kernel/*.mli

%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/async_kernel/*.a
%{_libdir}/ocaml/async_kernel/*.cmxa
%endif
%{_libdir}/ocaml/async_kernel/*.ml
%{_libdir}/ocaml/async_kernel/*.mli

%changelog
* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 111.28.00-1
- Initial package
