%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

# Select what subpackages to build.
%define build_mlvirsh                0

Name:           ocaml-libvirt
Version:        0.6.1.2
Release:        100%{?dist}%{?extra_release}
Summary:        OCaml binding for libvirt

License:        LGPLv2+
URL:            http://libvirt.org/ocaml/
Source0:        http://libvirt.org/sources/ocaml/%{name}-%{version}.tar.gz
Patch0:		ocaml-libvirt-1-252568550f9bf28b07f4e6d116485205e58afe4a
Patch1:		ocaml-libvirt-2-c6c9c3fff5993056e0af7219f4fe67ab8db3cdf2
Patch2:	 	ocaml-libvirt-3-34a472800ba1908e910318cc5d5ed9588174c1cf
Patch3:		ocaml-libvirt-4-9d178cbfeb709d2d2fbddb9fcab88e9204c8f995
Patch4:		ocaml-libvirt-5-2360cd228542c6a523f10daacbd631a753d17208
Patch5:		ocaml-libvirt-6-7568d6f77d72a77c527cc282511f7a3f37dc7040
Patch6:		ocaml-libvirt-7-71f683ad53e11c1f0cbc5c250d29647ad5ea0bf3
Patch7:		ocaml-libvirt-8-d7e0e6112db9411b0d7aaa8cbf5ce85c27e7d52d
Patch8:		ocaml-libvirt-9-0ec198e7784de1a49672183c961a2498b6c85b90
Patch9:		ocaml-libvirt-10-0d103e429ddc7942e537a047c8a46ca7ddc58e46
Patch10:	ocaml-libvirt-11-658970236caa31bbef44562c521d55b9a4689f4d
Patch11:	ocaml-libvirt-12-31ce6b280a2d987abc484b8f8d1e6cb25a70d737
Patch12:        ocaml-libvirt-13-fixbuild

ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel

BuildRequires:  libvirt-devel >= 0.2.1
BuildRequires:  perl
BuildRequires:  gawk

%description
OCaml binding for libvirt.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%if %build_mlvirsh
%package        -n mlvirsh
Summary:        OCaml virsh utility
License:        GPLv2+


%description    -n mlvirsh
OCaml virtualization shell.
%endif


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --libdir=%{_libdir} --prefix=%{_prefix}
make all doc
%if %opt
make opt
strip libvirt/dllmllibvirt.so
%endif


%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%if %opt
make install-opt
%else
make install-byte
%endif

%if !%build_mlvirsh
rm -f $RPM_BUILD_ROOT%{_bindir}/mlvirsh
%endif




%files
%doc COPYING.LIB README ChangeLog
%{_libdir}/ocaml/libvirt
%if %opt
%exclude %{_libdir}/ocaml/libvirt/*.a
%exclude %{_libdir}/ocaml/libvirt/*.cmxa
%exclude %{_libdir}/ocaml/libvirt/*.cmx
%endif
%exclude %{_libdir}/ocaml/libvirt/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc COPYING.LIB README TODO.libvirt ChangeLog html/*
%if %opt
%{_libdir}/ocaml/libvirt/*.a
%{_libdir}/ocaml/libvirt/*.cmxa
%{_libdir}/ocaml/libvirt/*.cmx
%endif
%{_libdir}/ocaml/libvirt/*.mli


%if %build_mlvirsh
%files -n mlvirsh
%doc COPYING README ChangeLog
%{_bindir}/mlvirsh
%endif


%changelog
* Tue May 13 2014 David Scott <dave.scott@citrix.com> - 0.6.1.2-100
- Bump release number to 100 to override upstream. Next release will
  have our patches applied.

* Fri Mar 23 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.2-1
- New upstream version 0.6.1.2.

* Tue Mar  6 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.1-1
- New upstream version 0.6.1.1.
- Remove mlvirsh subpackage, no longer upstream.
- Replace custom configure with RPM macro configure.
- Use RPM global instead of define.
- Use built-in RPM OCaml dependency generator.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-10
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-8
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-7
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-5
- Force rebuild to test FTBFS issue.

* Fri Jun 12 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-3
- Force rebuild to test FTBFS issue.

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-2
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar 10 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1.0-1
- New upstream release 0.6.1.0.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.4.2-3
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.4.2-2
- Rebuild for OCaml 3.11.0

* Wed Jul  9 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.4.2-1
- New upstream version.
- In upstream, 'make install' became 'make install-byte' or 'make install-opt'

* Tue Jun 10 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.2.4-1
- New upstream version.

* Thu Jun  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.2.3-1
- New upstream version.

* Thu Jun  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.2.2-1
- New upstream version.
- Removed virt-ctrl, virt-df, virt-top subpackages, since these are
  now separate Fedora packages.

* Tue May 20 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.1.1-4
- Disable virt-top (bz 442871).
- Disable virt-ctrl (bz 442875).

* Mon May 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.1.1-3
- Disable virt-df (bz 442873).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.1.1-2
- Rebuild for OCaml 3.10.2

* Tue Mar 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.1.1-1
- New upstream release 0.4.1.1.
- Move configure to build section.
- Pass RPM_OPT_FLAGS.

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.1.0-2
- Fix source URL.
- Install virt-df manpage.

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.1.0-1
- New upstream release 0.4.1.0.
- Upstream now requires ocaml-dbus >= 0.06, ocaml-lablgtk >= 2.10.0,
  ocaml-dbus-devel.
- Enable virt-df.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.0.3-3
- Rebuild for ppc64.

* Wed Feb 13 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.0.3-2
- Add BR gtk2-devel

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4.0.3-1
- New upstream version 0.4.0.3.
- Rebuild for OCaml 3.10.1.

* Tue Nov 20 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.3.4-1
- New upstream release 0.3.3.4.
- Upstream website is now http://libvirt.org/ocaml/

* Fri Oct 19 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.3.0-2
- Mistake: BR is ocaml-calendar-devel.

* Fri Oct 19 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.3.0-1
- New upstream release 0.3.3.0.
- Added support for virt-df, but disabled it by default.
- +BR ocaml-calendar.

* Mon Sep 24 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.8-1
- New upstream release 0.3.2.8.

* Thu Sep 20 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.7-1
- New upstream release 0.3.2.7.
- Ship the upstream ChangeLog file.

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.6-2
- Force dependency on ocaml >= 3.10.0-7 which has fixed requires/provides
  scripts.

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.6-1
- New upstream version 0.3.2.6.

* Wed Aug 29 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.5-1
- New upstream version 0.3.2.5.
- Keep TODO out of the main package, but add (renamed) TODO.libvirt and
  TODO.virt-top to the devel and virt-top packages respectively.
- Add BR gawk.

* Thu Aug 23 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.4-1
- New upstream version 0.3.2.4.

* Thu Aug 23 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.3-2
- build_* macros so we can choose what subpackages to build.

* Thu Aug 23 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.3-1
- Upstream version 0.3.2.3.
- Add missing BR libvirt-devel.

* Wed Aug 22 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.2-1
- Upstream version 0.3.2.2.

* Wed Aug 22 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.1-2
- Fix unclosed if-statement in spec file.

* Wed Aug 22 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.2.1-1
- Upstream version 0.3.2.1.
- Put HTML documentation in -devel package.

* Mon Aug  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.1.2-1
- Initial RPM release.
