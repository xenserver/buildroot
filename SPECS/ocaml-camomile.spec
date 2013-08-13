%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-camomile
Version:        0.8.3
Release:        10%{?dist}
Summary:        Unicode library for OCaml

# Several files are MIT and UCD licensed, but the overall work is LGPLv2+
# and the LGPL/GPL supercedes compatible licenses.
# https://www.redhat.com/archives/fedora-legal-list/2008-March/msg00005.html
License:        LGPLv2+
URL:            http://sourceforge.net/projects/camomile/
Source0:        http://downloads.sourceforge.net/camomile/camomile-%{version}.tar.bz2
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.12.1-12
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel


%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        data
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    data
The %{name}-data package contains data files for developing
applications that use %{name}.


%prep
%setup -q -n camomile-%{version}


%build
./configure --prefix=%{_prefix} --datadir=%{_datadir} --libdir=%{_libdir}
make
make dochtml
make man
strip tools/*.opt


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install prefix=$RPM_BUILD_ROOT%{_prefix} DATADIR=$RPM_BUILD_ROOT%{_datadir}
%if %opt
cp tools/camomilecharmap.opt $RPM_BUILD_ROOT%{_bindir}/camomilecharmap
cp tools/camomilelocaledef.opt $RPM_BUILD_ROOT%{_bindir}/camomilelocaledef
%endif


%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/ocaml/camomile
%if %opt
%exclude %{_libdir}/ocaml/camomile/*.a
%exclude %{_libdir}/ocaml/camomile/*.cmxa
%exclude %{_libdir}/ocaml/camomile/*.cmx
%endif
%exclude %{_libdir}/ocaml/camomile/*.mli
%if %opt
%{_bindir}/camomilecharmap
%{_bindir}/camomilelocaledef
%endif


%files devel
%defattr(-,root,root,-)
%doc README dochtml/*
%if %opt
%{_libdir}/ocaml/camomile/*.a
%{_libdir}/ocaml/camomile/*.cmxa
%{_libdir}/ocaml/camomile/*.cmx
%endif
%{_libdir}/ocaml/camomile/*.mli


%files data
%defattr(-,root,root,-)
%doc README
%{_datadir}/camomile/


%changelog
* Fri Oct 19 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-10
- Rebuild for OCaml 4.00.1.
- Clean up the spec file.

* Sat Jul 28 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-9
- Bump and rebuild against new OCaml 4.00.0 official release.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-7
- Rebuild for OCaml 4.00.0.

* Wed Jun  6 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-6
- Remove sed hack which worked around segfault on ppc64.  Now fixed
  in OCaml >= 3.12.1-12.

* Sun Jun  3 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-5
- Remove patch which worked around segfault on ARM.  Now fixed
  in OCaml >= 3.12.1-9.

* Wed May 30 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-4
- Remove ExcludeArch ppc64.
- Add sed hack to reduce size of long entry function which breaks
  ppc64 code generator.  See comment in spec file for full details.

* Sat May 19 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-2
- Include workaround for segfault in gen_mappings.ml on ARM.
- Bump release and rebuild for new OCaml on ARM.

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.3-1
- New upstream version 0.8.3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 0.8.1-1
- New upstream version 0.8.1.
- Rebuild for OCaml 3.12.0.
- camomilecharmap and camomilelocaledef no longer installed by default,
  install them by hand instead.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-2
- Rebuild for OCaml 3.11.2.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-1
- New upstream version 0.7.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-11
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-9
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-8
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-7
- Rebuild for OCaml 3.10.2

* Fri Mar 21 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-6
- ExcludeArch ppc64 (#438486).

* Mon Mar 17 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-5
- Definitive license.
- Move ./configure into the build section.
- Remove a superfluous comment in the install section.
- Fix rpmlint error 'configure-without-libdir-spec'.
- Scratch build in Koji.

* Wed Mar  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-4
- License is LGPLv2+ (no OCaml exception).

* Wed Mar  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-3
- Remove ExcludeArch ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-2
- Added BR ocaml-camlp4-devel.
- Rename /usr/bin/*.opt as /usr/bin.

* Wed Aug 08 2007 Richard W.M. Jones <rjones@redhat.com> - 0.7.1-1
- Initial RPM release.
