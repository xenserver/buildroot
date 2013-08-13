%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-bitstring
Version:        2.0.4
Release:        1%{?dist}
Summary:        OCaml library for matching and constructing bitstrings

Group:          Development/Libraries
License:        LGPLv2+ with exceptions and GPLv2+

URL:            http://code.google.com/p/bitstring/
Source0:        http://bitstring.googlecode.com/files/%{name}-%{version}.tar.gz

ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.2
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel

BuildRequires:  chrpath
BuildRequires:  time

%global __ocaml_requires_opts -i Asttypes -i Parsetree
%global __ocaml_provides_opts -i Pa_bitstring

# Upstream project used to be called ocaml-bitmatch.
# Keep these until Fedora 12.
Obsoletes:      ocaml-bitmatch <= 1.9.5
Provides:       ocaml-bitmatch = %{version}-%{release}


%description
Bitstring adds Erlang-style bitstrings and matching over bitstrings as
a syntax extension and library for OCaml.  You can use this module to
both parse and generate binary formats, for example, communications
protocols, disk formats and binary files.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

# Upstream project used to be called ocaml-bitmatch.
# Keep these until Fedora 12.
Obsoletes:      ocaml-bitmatch-devel <= 1.9.5
Provides:       ocaml-bitmatch-devel = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q

# Keep a pristine copy of the examples directory for distribution.
cp -a examples bitstring-examples


%build
%configure

# Doesn't build correctly with parallel builds, or if MAKEFLAGS=-j<N> is set.
make -j1

make doc
make examples


%check
make check


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

mkdir -p $RPM_BUILD_ROOT%{_bindir}

# Install bitstring-objinfo by hand for now.
install -m 0755 bitstring-objinfo $RPM_BUILD_ROOT%{_bindir}


%files
%doc COPYING.LIB
%{_libdir}/ocaml/bitstring
%if %opt
%exclude %{_libdir}/ocaml/bitstring/*.a
%exclude %{_libdir}/ocaml/bitstring/*.cmxa
%exclude %{_libdir}/ocaml/bitstring/*.cmx
%endif
%exclude %{_libdir}/ocaml/bitstring/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc COPYING.LIB README TODO html bitstring-examples
%if %opt
%{_libdir}/ocaml/bitstring/*.a
%{_libdir}/ocaml/bitstring/*.cmxa
%{_libdir}/ocaml/bitstring/*.cmx
%endif
%{_libdir}/ocaml/bitstring/*.mli
%{_bindir}/bitstring-objinfo


%changelog
* Tue May 14 2013 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-1
- New upstream version 2.0.4.
- Remove upstream patch to META file.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 2.0.3-5
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-4
- Remove defattr, clean etc for modern spec file.
- Permanently remove obsolete CIL tools.
- Add upstream patch to fix META file.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun  7 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-2
- Rebuild for OCaml 4.00.0.

* Tue Jan 17 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-1
- New upstream version 2.0.3.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-4
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-2
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Fri Jan  8 2010 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-1
- New upstream version 2.0.2.
- Remove the two patches which are now upstream.
- Replace %%define with %%global.
- Use upstream RPM 4.8 OCaml dependency generator.
- Recheck package with rpmlint.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-11
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-9
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-7
- Patch for OCaml 3.11.0 official.

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-6
- Rebuild.

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-5
- Disable CIL tools.
- Patch for OCaml 3.11.0.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-3
- Rebuild for OCaml 3.11.0

* Tue Oct 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-2
- Fixed incorrect sources file.

* Mon Oct 20 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-1
- Upstream released 2.0.0, requires OCaml 3.10.2 to compile.

* Tue Aug 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.8-3
- +BR time.

* Tue Aug 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.8-2
- New upstream release 1.9.8.
- Add *.so* files.

* Thu Jul 17 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.7-1
- New upstream release 1.9.7.
- Project renamed from ocaml-bitmatch to ocaml-bitstring.

* Fri Jul 11 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.5-1
- New upstream release 1.9.5.
- Clarify that the programs have GPL license.
- Ship bitmatch-objinfo program.

* Fri Jul  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.4-1
- New upstream release 1.9.4.

* Fri Jul  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.3-2
- New upstream release 1.9.3.
- Don't build CIL tools unless we have CIL.

* Tue Jul  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-3
- +BR ocaml-extlib-devel.

* Tue Jul  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-2
- Force rebuild, forgot sources first time.

* Tue Jul  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-1
- New upstream release 1.9.2.
- Include C tools (requiring CIL) in a separate subpackage.

* Wed May 21 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-1
- New upstream release 1.3.

* Sun May 18 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2-1
- New upstream release 1.2.
- Build and distribute the examples.
- Distribute the TODO file.

* Sun May 18 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0-3
- New upstream release 1.0.
- New upstream URL and download location.
- Use RPM percent-configure in build section.

* Mon May 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9-1
- New upstream release 0.9.

* Thu May  8 2008 Richard W.M. Jones <rjones@redhat.com> - 0.8-1
- New upstream release 0.8.

* Wed May  7 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7-3
- New upstream release 0.7.

* Fri Apr 25 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6-1
- New upstream release 0.6.

* Fri Apr 25 2008 Richard W.M. Jones <rjones@redhat.com> - 0.5-1
- New upstream release 0.5.

* Fri Apr 16 2008 Richard W.M. Jones <rjones@redhat.com> - 0.4-1
- New upstream release 0.4.

* Fri Apr  2 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2-1
- Initial RPM release.
