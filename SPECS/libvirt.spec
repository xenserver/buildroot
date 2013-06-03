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
