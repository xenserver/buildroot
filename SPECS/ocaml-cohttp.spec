%global debug_package %{nil}

Name:           ocaml-cohttp
Version:        0.11.2
Release:        1%{?dist}
Summary:        An HTTP library for OCaml
License:        LGPL
URL:            https://github.com/mirage/ocaml-cohttp
Source0:        https://github.com/mirage/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-ssl-devel
BuildRequires:  ocaml-uri-devel
BuildRequires:  ocaml-stringext-devel
BuildRequires:  ocaml-conduit-devel
BuildRequires:  ocaml-fieldslib-devel
BuildRequires:  ocaml-sexplib-devel

%description
An HTTP library for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-ssl-devel%{?_isa}
Requires:       ocaml-uri-devel%{?_isa}
Requires:       ocaml-stringext-devel%{?_isa}
Requires:       ocaml-conduit-devel%{?_isa}
Requires:       ocaml-fieldslib-devel%{?_isa}
Requires:       ocaml-sexplib-devel%{?_isa}

%package	bin
Summary:        Example binaries for %{name}

%description    bin
The %{name}-bin package contains the compiled example files
for %{name}.

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q 

%build
# Dirty hack
export PREFIX=%{buildroot}%{_prefix}
make build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/cohttp
%exclude %{_libdir}/ocaml/cohttp/*.a
%exclude %{_libdir}/ocaml/cohttp/*.cmxa
%exclude %{_libdir}/ocaml/cohttp/*.cmx
%exclude %{_libdir}/ocaml/cohttp/*.mli

%files devel
%{_libdir}/ocaml/cohttp/*.a
%{_libdir}/ocaml/cohttp/*.cmx
%{_libdir}/ocaml/cohttp/*.cmxa
%{_libdir}/ocaml/cohttp/*.mli

%files bin
%{_prefix}/bin/cohttp-server-lwt

%changelog
* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.11.2-1
- Update to 0.11.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.8-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.8-1
- Initial package

