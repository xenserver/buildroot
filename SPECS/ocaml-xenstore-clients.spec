%global debug_package %{nil}

Name:           ocaml-xenstore-clients
Version:        0.9.3
Release:        2%{?dist}
Summary:        Unix xenstore clients for OCaml
License:        LGPL
URL:            https://github.com/xapi-project/ocaml-xenstore-clients
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-xenstore-devel

%description
Unix xenstore clients for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-xenstore-devel%{?_isa}

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
make install DESTDIR=${buildroot}


%files
%doc LICENSE 
%doc MAINTAINERS
%doc README.md 
%{_libdir}/ocaml/xenstore_transport
%exclude %{_libdir}/ocaml/xenstore_transport/*.a
%exclude %{_libdir}/ocaml/xenstore_transport/*.cmxa
%exclude %{_libdir}/ocaml/xenstore_transport/*.cmx

%files devel
%{_libdir}/ocaml/xenstore_transport/*.a
%{_libdir}/ocaml/xenstore_transport/*.cmxa
%{_libdir}/ocaml/xenstore_transport/*.cmx

%changelog
* Mon Jun  2 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Split files correctly between base and devel packages

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.3-1
- Update to 0.9.3

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

