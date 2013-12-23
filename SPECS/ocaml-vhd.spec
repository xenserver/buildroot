%global debug_package %{nil}

Name:           ocaml-vhd
Version:        0.6.4
Release:        1
Summary:        Pure OCaml library for reading, writing, streaming, converting vhd format files
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Libraries
URL:            http://github.com/djs55/ocaml-vhd
Source0:        https://github.com/djs55/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib cmdliner-devel ocaml-ounit-devel ocaml-cstruct-devel ocaml-lwt-devel ocaml-uuidm-devel ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib

%description
A pure OCaml parser and printer for vhd format data. The library allows
vhd files to be read, written and streamed with on-the-fly format conversion.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

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
# This space intentionally left blank

%files devel
%doc CHANGES README.md LICENSE

%{_libdir}/ocaml/vhd-format/*
%{_libdir}/ocaml/stublibs/dllvhd*

%changelog
* Thu Nov 21 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.4-1
- Update to 0.6.4

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.1-1
- Update to 0.6.1

* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Initial package

