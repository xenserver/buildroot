Name:           ocaml-nbd
Version:        1.0.2
Release:        1%{?dist}
Summary:        Pure OCaml implementation of the Network Block Device protocol
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/nbd
Source0:        https://github.com/xapi-project/nbd/archive/v%{version}/nbd-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lwt-devel

%description
An implementation of the Network Block Device protocol for both
regular Unix and Lwt in OCaml. This library allows applications to
access remote block devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  ocaml-cstruct-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n nbd-%{version}

%build
./configure --prefix %{_prefix} --destdir %{buildroot}
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{_bindir}/nbd-tool
%{_libdir}/ocaml/nbd
%exclude %{_libdir}/ocaml/nbd/*.a
%exclude %{_libdir}/ocaml/nbd/*.cmxa
%exclude %{_libdir}/ocaml/nbd/*.cmx
%exclude %{_libdir}/ocaml/nbd/*.ml
%exclude %{_libdir}/ocaml/nbd/*.mli

%files devel
%{_libdir}/ocaml/nbd/*.a
%{_libdir}/ocaml/nbd/*.cmx
%{_libdir}/ocaml/nbd/*.cmxa
%{_libdir}/ocaml/nbd/*.mli

%changelog
* Mon Mar 31 2014 Euan Harris <euan.harris@citrix.com> - 1.0.2-1
- Update to 1.0.2, removing dependency on ocaml-obuild

* Thu Nov 21 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

