%define debug_package %{nil}

Name:           ocaml-mirage-block-xen
Version:        1.1.0
Release:        1%{?dist}
Summary:        Mirage block driver for Xen that implements the blkfront/back protocol
License:        ISC
URL:            https://github.com/mirage/mirage-block-xen/
Source0:        https://github.com/mirage/mirage-block-xen/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-shared-memory-ring-devel
BuildRequires:  ocaml-ipaddr-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-mirage-xen-devel

%description
Mirage block driver for Xen that implements the blkfront/back protocol

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-block-xen-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/mirage-block-xen
%exclude %{_libdir}/ocaml/mirage-block-xen/*.a
%exclude %{_libdir}/ocaml/mirage-block-xen/*.cmxa
%exclude %{_libdir}/ocaml/mirage-block-xen/*.cmx
%exclude %{_libdir}/ocaml/mirage-block-xen/*.ml
%exclude %{_libdir}/ocaml/mirage-block-xen/*.mli

%files devel
%{_libdir}/ocaml/mirage-block-xen/*.a
%{_libdir}/ocaml/mirage-block-xen/*.cmx
%{_libdir}/ocaml/mirage-block-xen/*.cmxa
%{_libdir}/ocaml/mirage-block-xen/*.mli

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 1.0.5-1
- Initial package
