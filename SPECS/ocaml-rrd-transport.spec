%define debug_package %{nil}

Name:           ocaml-rrd-transport
Version:        0.7.1
Release:        1%{?dist}
Summary:        Shared-memory protocols for transmitting RRD data
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/rrd-transport/
Source0:        https://github.com/xapi-project/rrd-transport/archive/%{version}/%{name}-%{version}.tar.gz
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/ocaml/rrd-transport/META
%{_libdir}/ocaml/rrd-transport/rrd_transport.cma
%{_libdir}/ocaml/rrd-transport/rrd_io.cmi
%{_libdir}/ocaml/rrd-transport/rrd_json.cmi
%{_libdir}/ocaml/rrd-transport/rrd_protocol.cmi
%{_libdir}/ocaml/rrd-transport/rrd_protocol_v1.cmi
%{_libdir}/ocaml/rrd-transport/rrd_protocol_v2.cmi
%{_libdir}/ocaml/rrd-transport/rrd_reader.cmi
%{_libdir}/ocaml/rrd-transport/rrd_rpc.cmi
%{_libdir}/ocaml/rrd-transport/rrd_writer.cmi

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md
%{_libdir}/ocaml/rrd-transport/rrd_transport.a
%{_libdir}/ocaml/rrd-transport/rrd_transport.cmxa
%{_libdir}/ocaml/rrd-transport/rrd_transport.cmxs
%{_libdir}/ocaml/rrd-transport/rrd_io.cmx
%{_libdir}/ocaml/rrd-transport/rrd_io.mli
%{_libdir}/ocaml/rrd-transport/rrd_json.cmx
%{_libdir}/ocaml/rrd-transport/rrd_json.mli
%{_libdir}/ocaml/rrd-transport/rrd_protocol.cmx
%{_libdir}/ocaml/rrd-transport/rrd_protocol.mli
%{_libdir}/ocaml/rrd-transport/rrd_protocol_v1.cmx
%{_libdir}/ocaml/rrd-transport/rrd_protocol_v1.mli
%{_libdir}/ocaml/rrd-transport/rrd_protocol_v2.cmx
%{_libdir}/ocaml/rrd-transport/rrd_protocol_v2.mli
%{_libdir}/ocaml/rrd-transport/rrd_reader.cmx
%{_libdir}/ocaml/rrd-transport/rrd_reader.mli
%{_libdir}/ocaml/rrd-transport/rrd_rpc.cmx
%{_libdir}/ocaml/rrd-transport/rrd_rpc.mli
%{_libdir}/ocaml/rrd-transport/rrd_writer.cmx
%{_libdir}/ocaml/rrd-transport/rrd_writer.mli

%changelog
* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 0.7.1-1
- Update to 0.7.1

* Mon Dec 16 2013 John Else <john.else@citrix.com> - 0.5.0-1
- Initial package
