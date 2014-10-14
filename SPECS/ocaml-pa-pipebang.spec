%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

%define dlnode  832

Name:           ocaml-pa-pipebang
Version:        109.28.02
Release:        1%{?dist}
Summary:        Syntax extension to transform x |! f into f x

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/pipebang
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/pipebang-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
This package contains a simple syntax extension that transforms
x |! f onto f x.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pipebang-%{version}
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
%{_libdir}/ocaml/pa_pipebang
%if %opt
%exclude %{_libdir}/ocaml/pa_pipebang/*.a
%exclude %{_libdir}/ocaml/pa_pipebang/*.cmxa
%endif
%exclude %{_libdir}/ocaml/pa_pipebang/*.ml


%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/pa_pipebang/*.a
%{_libdir}/ocaml/pa_pipebang/*.cmxa
%endif
%{_libdir}/ocaml/pa_pipebang/*.ml


%changelog
* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.28.02-1
- Initial package for Fedora 20
