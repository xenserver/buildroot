%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-textutils
Version:        112.01.00
Release:        1%{?dist}
Summary:        Syntax extension for inserting the current location.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/textutils
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/textutils-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-async-devel
BuildRequires:  ocaml-core-devel
BuildRequires:  ocaml-pa-ounit-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-enumerate-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Syntax extension for inserting the current location.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n textutils-%{version}

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
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%{_libdir}/ocaml/textutils
%if %opt
%exclude %{_libdir}/ocaml/textutils/*.a
%exclude %{_libdir}/ocaml/textutils/*.cmxa
%endif
%exclude %{_libdir}/ocaml/textutils/*.ml
%exclude %{_libdir}/ocaml/textutils/*.mli


%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/textutils/*.a
%{_libdir}/ocaml/textutils/*.cmxa
%endif
%{_libdir}/ocaml/textutils/*.ml
%{_libdir}/ocaml/textutils/*.mli


%changelog
* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 112.01.00-1
- Update to 112.01.00

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.35.02-1
- Initial package for Fedora 20.
