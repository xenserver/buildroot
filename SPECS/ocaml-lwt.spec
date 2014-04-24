%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-lwt
Version:        2.4.3
Release:        1%{?dist}
Summary:        OCaml lightweight thread library

Group:          Development/Libraries
License:        LGPLv2+ with exceptions
URL:            http://ocsigen.org/lwt
Source0:        http://ocsigen.org/download/lwt-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x

# Location of libev headers on Fedora is in /usr/include/libev/ev.h
# so we need to patch the source accordingly.
#Patch0:         lwt-2.2.0-libev.patch

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-react-devel >= 0.9.0
#BuildRequires:  libev-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-text-devel
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ssl-devel

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n lwt-%{version}

#%patch0 -p1

mv README README.old
iconv -f iso-8859-1 -t utf-8 < README.old > README


%build
export C_INCLUDE_PATH=/usr/include/libev
./configure --enable-react --enable-text --disable-libev --enable-ssl
make


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install
mkdir -p $RPM_BUILD_ROOT%{_bindir}

strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
#chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so



%files
# This space intentionally left blank

%files devel
%doc LICENSE COPYING CHANGES README
%{_libdir}/ocaml/lwt/*
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%changelog
* Sat Jun  1 2013 David Scott <dave.scott@eu.citrix.com> - 2.4.3-1
- Update to 2.4.3

* Wed Nov  2 2011 David Scott <dave.scott@eu.citrix.com> - 2.2.0-2
- Rebuilt for XCP

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-1
- New upstream version 2.2.0.
- Rebuild for OCaml 3.12.0.
- Add BR libev-devel.
- Patch <ev.h> -> <libev/ev.h>
- *.cmx files are no longer being distributed.
- No VERSION file.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.3.rc1
- Rebuild for OCaml 3.11.2.

* Mon Oct 12 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.2.rc1.fc13
- ocaml-react is now in Fedora, so build this package.
- Missing BR on camlp4.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.rc1.fc13
- New upstream version 2.0.0+rc1.
- NB. This cannot be built as it depends on new package ocaml-react
  (RHBZ#527971).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-5
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-3
- Rebuild.

* Wed Sep  3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- Rebuild with higher EVR than F-9 branch.

* Mon Sep  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- Initial RPM release.
