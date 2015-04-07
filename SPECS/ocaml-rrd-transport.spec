%define debug_package %{nil}

Name:           ocaml-rrd-transport
Version:        0.8.0
Release:        1%{?dist}
Summary:        Shared-memory protocols for transmitting RRD data
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/rrd-transport/
Source0:        https://github.com/xapi-project/rrd-transport/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-crc-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-gnt-devel
Requires:       ocaml
Requires:       ocaml-findlib

%description
Shared-memory protocol for transmitting RRD data, supporting in-memory files
and shared Xen pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-gnt-devel
Requires:       ocaml-crc-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n rrd-transport-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%files
%doc LICENSE
%{_libdir}/ocaml/rrd-transport
%exclude %{_libdir}/ocaml/rrd-transport/*.a
%exclude %{_libdir}/ocaml/rrd-transport/*.cmxa
%exclude %{_libdir}/ocaml/rrd-transport/*.cmx
%exclude %{_libdir}/ocaml/rrd-transport/*.mli
%exclude %{_libdir}/ocaml/rrd-transport/*.cmt
%exclude %{_libdir}/ocaml/rrd-transport/*.cmti
%exclude %{_libdir}/ocaml/rrd-transport/*.annot

%files devel
%doc ChangeLog README.md
%{_libdir}/ocaml/rrd-transport/*.a
%{_libdir}/ocaml/rrd-transport/*.cmx
%{_libdir}/ocaml/rrd-transport/*.cmxa
%{_libdir}/ocaml/rrd-transport/*.mli

%changelog
* Sat Apr  4 2015 David Scott <dave.scott@citrix.com> - 0.8.0-1
- Update to 0.8.0

* Fri Oct 24 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.7.2-1
- Update to 0.7.2

* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 0.7.1-1
- Update to 0.7.1

* Mon Dec 16 2013 John Else <john.else@citrix.com> - 0.5.0-1
- Initial package
