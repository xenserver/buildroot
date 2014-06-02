Name:           ocaml-sha
Version:        1.9
Release:        2%{?dist}
Summary:        OCaml SHA
License:        LGPL2.1
URL:            https://github.com/vincenthz/ocaml-sha
Source0:        https://github.com/xapi-project/ocaml-sha/archive/ocaml-sha-v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
This is a set of C bindings for computing SHA digests.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-v%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc README
%{_libdir}/ocaml/sha
%exclude %{_libdir}/ocaml/sha/*.a
%exclude %{_libdir}/ocaml/sha/*.cmxa
%exclude %{_libdir}/ocaml/sha/*.cmx

%files devel
%{_libdir}/ocaml/sha/*.a
%{_libdir}/ocaml/sha/*.cmx
%{_libdir}/ocaml/sha/*.cmxa

%changelog
* Tue Apr 22 2014 Euan Harris <euan.harris@citrix.com> - 1.9-2
- Split files correctly between base and devel packages

* Mon Nov 18 2013 David Scott <dave.scott@eu.citrix.com> - 1.9-1
- Initial package

