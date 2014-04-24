Name:           ocaml-tar
Version:        0.2.1
Release:        1%{?dist}
Summary:        OCaml parser and printer for tar-format data
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Libraries
URL:            http://github.com/djs55/ocaml-tar
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz 
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-camlp4-devel

%description
This is a pure OCaml library for reading and writing tar-format data.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%doc README.md

%{_libdir}/ocaml/tar/META
%{_libdir}/ocaml/tar/tar.a
%{_libdir}/ocaml/tar/tar.cma
%{_libdir}/ocaml/tar/tar.cmi
%{_libdir}/ocaml/tar/tar.cmx
%{_libdir}/ocaml/tar/tar.cmxa
%{_libdir}/ocaml/tar/tar.cmxs
%{_libdir}/ocaml/tar/tar.mli
%{_libdir}/ocaml/tar/tar_lwt_unix.a
%{_libdir}/ocaml/tar/tar_lwt_unix.cma
%{_libdir}/ocaml/tar/tar_lwt_unix.cmi
%{_libdir}/ocaml/tar/tar_lwt_unix.cmx
%{_libdir}/ocaml/tar/tar_lwt_unix.cmxa
%{_libdir}/ocaml/tar/tar_lwt_unix.cmxs
%{_libdir}/ocaml/tar/tar_lwt_unix.mli
%{_libdir}/ocaml/tar/tar_unix.a
%{_libdir}/ocaml/tar/tar_unix.cma
%{_libdir}/ocaml/tar/tar_unix.cmi
%{_libdir}/ocaml/tar/tar_unix.cmx
%{_libdir}/ocaml/tar/tar_unix.cmxa
%{_libdir}/ocaml/tar/tar_unix.cmxs
%{_libdir}/ocaml/tar/tar_unix.mli

%changelog
* Fri Nov 15 2013 David Scott <dave.scott@eu.citrix.com> - 0.2.1-1
- Initial package
