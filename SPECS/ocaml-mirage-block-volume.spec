%define debug_package %{nil}

Name:           ocaml-mirage-block-volume
Version:        0.9.1
Release:        1%{?dist}
Summary:        Mirage volume library compatible with LVM
License:        ISC
URL:            https://github.com/mirage/mirage-block-volume/
Source0:        https://github.com/mirage/mirage-block-volume/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-kaputt-devel
BuildRequires:  ocaml-shared-block-ring-devel
BuildRequires:  ocaml-mirage-block-unix-devel
BuildRequires:  ocaml-mirage-clock-unix-devel
BuildRequires:  ocaml-cmdliner-devel

%description
A Linux-LVM compatible logical volume manager for mirage

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-block-volume-%{version}

%build
make all

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%doc CHANGES
%doc README.md
%doc LICENSE
%{_libdir}/ocaml/lvm
%exclude %{_libdir}/ocaml/lvm/*.a
%exclude %{_libdir}/ocaml/lvm/*.cmxa
%exclude %{_libdir}/ocaml/lvm/*.cmx
%exclude %{_libdir}/ocaml/lvm/*.mli
%{_libdir}/ocaml/lvm_internal
%exclude %{_libdir}/ocaml/lvm_internal/*.a
%exclude %{_libdir}/ocaml/lvm_internal/*.cmxa
%exclude %{_libdir}/ocaml/lvm_internal/*.cmx

%files devel
%{_libdir}/ocaml/lvm/*.a
%{_libdir}/ocaml/lvm/*.cmx
%{_libdir}/ocaml/lvm/*.cmxa
%{_libdir}/ocaml/lvm/*.mli
%{_libdir}/ocaml/lvm_internal/*.a
%{_libdir}/ocaml/lvm_internal/*.cmx
%{_libdir}/ocaml/lvm_internal/*.cmxa

%changelog
* Sun Apr 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-1
- Initial package
