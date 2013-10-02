%global debug_package %{nil}

Name:           ocaml-vhd
Version:        0.6.0
Release:        1
Summary:        A pure OCaml library for reading, writing, streaming, converting vhd format files
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/djs55/ocaml-vhd
Source0:        https://github.com/djs55/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib cmdliner-devel ocaml-ounit-devel ocaml-cstruct-devel ocaml-lwt-devel ocaml-uuidm-devel ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib

%description
A pure OCaml parser and printer for vhd format data. The library allows
vhd files to be read, written and streamed with on-the-fly format conversion.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc CHANGES README.md LICENSE

%{_libdir}/ocaml/vhd-format/*
%{_libdir}/ocaml/stublibs/dllvhd*

%changelog
* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Initial package

