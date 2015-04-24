Name:           ocaml-mtime
Version:        0.8.1
Release:        1%{?dist}
Summary:        Monotonic wall-clock time for OCaml
License:        BSD3
URL:            http://erratique.ch/software/mtime
Source0:        http://erratique.ch/software/mtime/releases/mtime-%{version}.tbz
Patch0:         mtime-no-js.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
Mtime is an OCaml module to access monotonic wall-clock time. It
allows to measure time spans without being subject to operating system
calendar time adjustments.

Mtime depends only on your platform system library. The optional
JavaScript support depends on [js_of_ocaml][1]. It is distributed
under the BSD3 license.

[1]: http://ocsigen.org/js_of_ocaml/

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mtime-%{version}
%patch0 -p1

%build
ocaml pkg/git.ml
ocaml pkg/build.ml native=true native-dynlink=true jsoo=false

%install
find .
mkdir -p %{buildroot}/%{_libdir}/ocaml/mtime
mkdir -p %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/pkg/META %{buildroot}/%{_libdir}/ocaml/mtime
cp _build/src-os/mtime.a %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.cma %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.cmi %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.cmti %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.cmx %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.cmxa %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.cmxs %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime.mli %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/libmtime_stubs.a %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/dllmtime_stubs.so %{buildroot}/%{_libdir}/ocaml/mtime

cp _build/src-os/mtime_top.a %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime_top.cma %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime_top.cmxa %{buildroot}/%{_libdir}/ocaml/mtime/os
cp _build/src-os/mtime_top.cmxs %{buildroot}/%{_libdir}/ocaml/mtime/os

%files
%doc _build/CHANGES.md
%doc _build/README.md
%{_libdir}/ocaml/mtime
%{_libdir}/ocaml/mtime/os
%exclude %{_libdir}/ocaml/mtime/os/*.a
%exclude %{_libdir}/ocaml/mtime/os/*.cmxa
%exclude %{_libdir}/ocaml/mtime/os/*.cmx
%exclude %{_libdir}/ocaml/mtime/os/*.mli

%files devel
%{_libdir}/ocaml/mtime/os/*.a
%{_libdir}/ocaml/mtime/os/*.cmxa
%{_libdir}/ocaml/mtime/os/*.cmx
%{_libdir}/ocaml/mtime/os/*.mli

%changelog
* Fri Apr 24 2015 David Scott <dave.scott@citrix.com> - 0.8.1-1
- Initial package
