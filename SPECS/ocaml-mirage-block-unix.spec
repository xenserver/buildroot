%define debug_package %{nil}

Name:           ocaml-mirage-block-unix
Version:        1.2.2
Release:        1%{?dist}
Summary:        Mirage block driver for Unix that implements the blkfront/back protocol
License:        ISC
URL:            https://github.com/mirage/mirage-block-unix/
Source0:        https://github.com/mirage/mirage-block-unix/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-ounit-devel

%description
Mirage block driver for Unix that implements the blkfront/back protocol

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-block-unix-%{version}

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
%{_libdir}/ocaml/mirage-block-unix
%exclude %{_libdir}/ocaml/mirage-block-unix/*.a
%exclude %{_libdir}/ocaml/mirage-block-unix/*.cmxa
%exclude %{_libdir}/ocaml/mirage-block-unix/*.cmx
%exclude %{_libdir}/ocaml/mirage-block-unix/*.mli

%files devel
%{_libdir}/ocaml/mirage-block-unix/*.a
%{_libdir}/ocaml/mirage-block-unix/*.cmx
%{_libdir}/ocaml/mirage-block-unix/*.cmxa
%{_libdir}/ocaml/mirage-block-unix/*.mli

%changelog
* Sun Apr 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.1-1
- Initial package
