%global debug_package %{nil}

Name:           ocaml-vhd
Version:        0.7.2
Release:        1%{?dist}
Summary:        Pure OCaml library for reading, writing, streaming, converting vhd format files
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/djs55/ocaml-vhd
Source0:        https://github.com/djs55/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-mirage-types-devel

%description
A pure OCaml parser and printer for vhd format data. The library allows
vhd files to be read, written and streamed with on-the-fly format conversion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-io-page-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-ounit-devel%{?_isa}
Requires:       ocaml-mirage-types-devel%{?_isa}
Requires:       ocaml-uuidm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# The auto-requirements script can't handle packed libraries.
%{?filter_setup:
%filter_from_requires /ocaml(Patterns)/d
%filter_from_requires /ocaml(S)/d
%filter_setup
}


%prep
%setup -q

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install


%files
%doc CHANGES
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/vhd-format
%{_libdir}/ocaml/stublibs/dllvhd*
%exclude %{_libdir}/ocaml/vhd-format/*.a
%exclude %{_libdir}/ocaml/vhd-format/*.cmxa
%exclude %{_libdir}/ocaml/vhd-format/*.cmx
%exclude %{_libdir}/ocaml/vhd-format/*.ml
%exclude %{_libdir}/ocaml/vhd-format/*.mli


%files devel
%{_libdir}/ocaml/vhd-format/*.a
%{_libdir}/ocaml/vhd-format/*.cmx
%{_libdir}/ocaml/vhd-format/*.cmxa
%{_libdir}/ocaml/vhd-format/*.mli


%changelog
* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.7.2-1
- Update to 0.7.2

* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 0.7.0-1
- Update to 0.7.0

* Thu Nov 21 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.4-1
- Update to 0.6.4

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.1-1
- Update to 0.6.1

* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Initial package

