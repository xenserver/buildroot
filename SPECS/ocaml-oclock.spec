%define debug_package %{nil}

Name:           ocaml-oclock
Version:        0.3
Release:        3%{?dist}
Summary:        POSIX monotonic clock for OCaml
License:        ISC
URL:            https://github.com/polazarus/oclock
Source0:        https://github.com/polazarus/oclock/archive/v0.3/oclock-%{version}.tar.gz
Patch0:         oclock-1-cc-headers
Patch1:         oclock-2-destdir
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
A POSIX monotonic clock for OCaml

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n oclock-%{version}
%patch0 -p1
%patch1 -p1

%build
make

%install
export OCAMLFIND_DISTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DISTDIR
mkdir -p $OCAMLFIND_DISTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%files
%doc LICENSE
%doc README.markdown
%{_libdir}/ocaml/oclock
%exclude %{_libdir}/ocaml/oclock/*.a
%exclude %{_libdir}/ocaml/oclock/*.cmxa
%{_libdir}/ocaml/stublibs/dlloclock.so
%{_libdir}/ocaml/stublibs/dlloclock.so.owner

%files devel
%{_libdir}/ocaml/oclock/*.a
%{_libdir}/ocaml/oclock/*.cmxa

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.3-3
- Split files correctly between base and devel packages

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.3-2
- Initial package

