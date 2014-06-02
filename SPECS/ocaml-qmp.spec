%global debug_package %{nil}

Name:           ocaml-qmp
Version:        0.9.2
Release:        2%{?dist}
Summary:        Pure OCaml implementation of the Qemu Message Protocol (QMP)
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/ocaml-qmp
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-yojson-devel

%description
An implementation of the Qemu Message Protocol (QMP) that allows
an application to command, and receive events from, a running qemu
process.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-yojson-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%files
%doc ChangeLog
%doc README.md
%doc LICENSE
%{_libdir}/ocaml/qmp
%exclude %{_libdir}/ocaml/qmp/*.a
%exclude %{_libdir}/ocaml/qmp/*.cmxa
%exclude %{_libdir}/ocaml/qmp/*.cmx

%files devel
%{_libdir}/ocaml/qmp/*.a
%{_libdir}/ocaml/qmp/*.cmx
%{_libdir}/ocaml/qmp/*.cmxa

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.2-2
- Split files correctly between base and devel packages

* Thu Mar 27 2014 Euan Harris <euan.harris@citrix.com> - 0.9.2-1
- Add support for QMP 'change' command, used to change removable media
  and reconfigure VNC.

* Fri Aug 09 2013 Euan Harris <euan.harris@citrix.com> - 0.9.1-1
- Change representation of message timestamps from a tuple of ints to
  a float.  This avoids problems on 32-bit architectures and  follows
  the example of the OCaml standard library.

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

