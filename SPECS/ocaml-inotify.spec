%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-inotify
Version:        1.3
Release:        1%{?dist}
Summary:        Inotify bindings for OCaml.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://bitbucket.org/seanmcl/ocaml-inotify
Source0:        https://bitbucket.org/seanmcl/ocaml-inotify/get/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  chrpath


%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Inotify bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n seanmcl-ocaml-inotify-97ffca4c739e
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
%doc LICENSE
%{_libdir}/ocaml/inotify
%if %opt
%exclude %{_libdir}/ocaml/inotify/*.a
%exclude %{_libdir}/ocaml/inotify/*.cmxa
%endif
%exclude %{_libdir}/ocaml/inotify/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner
%{_bindir}/test-inotify

%files devel
%defattr(-,root,root,-)
%doc LICENSE
%if %opt
%{_libdir}/ocaml/inotify/*.a
%{_libdir}/ocaml/inotify/*.cmxa
%endif
%{_libdir}/ocaml/inotify/*.mli

%changelog
* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 1.3-1
- Initial package for Fedora 20.
