%define debug_package %{nil}

Name:           ocaml-testvmlib
Version:        0.4
Release:        1%{?dist}
Summary:        Mirage test VM library
License:        ISC
URL:            https://github.com/mirage/testvm-idl/
Source0:        https://github.com/mirage/testvm-idl/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-evtchn-devel
BuildRequires:  xen-devel
BuildRequires:  ocaml-gnt-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-vchan-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-mirage-devel
BuildRequires:  ocaml-ipaddr-devel

%description
An interface definition, library and command-line tool for Mirage VM testing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-io-page-devel%{?_isa}
Requires:       ocaml-mirage-devel%{?_isa}
Requires:       xen-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n testvm-idl-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install
mkdir %{buildroot}%{_bindir}
cp client.native %{buildroot}%{_bindir}/mirage-testvm-cli

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/testvmlib
%exclude %{_libdir}/ocaml/testvmlib/*.a
%exclude %{_libdir}/ocaml/testvmlib/*.cmxa
%exclude %{_libdir}/ocaml/testvmlib/*.cmx
%exclude %{_libdir}/ocaml/testvmlib/*.ml
%{_bindir}/mirage-testvm-cli

%files devel
%{_libdir}/ocaml/testvmlib/*.a
%{_libdir}/ocaml/testvmlib/*.cmx
%{_libdir}/ocaml/testvmlib/*.cmxa

%changelog
* Fri Apr  3 2015 David Scott <dave.scott@citrix.com> - 0.4-1
- Update to 0.4

* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 0.3-1
- Update to 0.3

* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 0.2-1
- Initial package
