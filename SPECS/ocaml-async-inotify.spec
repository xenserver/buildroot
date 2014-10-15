%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-async-inotify
Version:        111.28.00
Release:        1%{?dist}
Summary:        Jane Street Capital's asynchronous execution library (core)

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/async_inotify
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/async_inotify-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-async-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-comparelib-devel
BuildRequires:  ocaml-enumerate-devel
BuildRequires:  ocaml-herelib-devel
BuildRequires:  ocaml-custom-printf-devel
BuildRequires:  ocaml-async-find-devel
BuildRequires:  ocaml-inotify-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Jane Street Capital's asynchronous execution library (core).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n async_inotify-%{version}

%build
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
%{_libdir}/ocaml/async_inotify
%if %opt
%exclude %{_libdir}/ocaml/async_inotify/*.a
%exclude %{_libdir}/ocaml/async_inotify/*.cmxa
%endif
%exclude %{_libdir}/ocaml/async_inotify/*.mli

%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/async_inotify/*.a
%{_libdir}/ocaml/async_inotify/*.cmxa
%endif
%{_libdir}/ocaml/async_inotify/*.mli

%changelog
* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 111.28.00-1
- Update to 111.28.00

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.34.02-1
- Initial package for Fedora 20.
