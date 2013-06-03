%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

# Select what subpackages to build.
%define build_mlvirsh                0

Name:           ocaml-libvirt
Version:        0.6.1.2
Release:        1%{?dist}%{?extra_release}
Summary:        OCaml binding for libvirt

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://libvirt.org/ocaml/
Source0:        http://libvirt.org/sources/ocaml/ocaml-libvirt-%{version}.tar.gz
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

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel

BuildRequires:  libvirt-devel >= 0.2.1
BuildRequires:  perl
BuildRequires:  gawk

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh

%description
OCaml binding for libvirt.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%if %build_mlvirsh
%package        -n mlvirsh
Summary:        OCaml virsh utility
Group:          Applications/Emulators
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
rm -rf $RPM_BUILD_ROOT
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


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%doc COPYING.LIB README TODO.libvirt ChangeLog html/*
%if %opt
%{_libdir}/ocaml/libvirt/*.a
%{_libdir}/ocaml/libvirt/*.cmxa
%{_libdir}/ocaml/libvirt/*.cmx
%endif
%{_libdir}/ocaml/libvirt/*.mli


%if %build_mlvirsh
%files -n mlvirsh
%defattr(-,root,root,-)
%doc COPYING README ChangeLog
%{_bindir}/mlvirsh
%endif


%changelog
