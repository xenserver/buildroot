Name:           ocaml-ipaddr
Version:        2.4.0
Release:        1%{?dist}
Summary:        Pure OCaml implementation of the Network Block Device protocol
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/mirage/ocaml-ipaddr
Source0:        https://github.com/mirage/ocaml-ipaddr/archive/%{version}/ocaml-ipaddr-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
An implementation of the Network Block Device protocol for both
regular Unix and Lwt in OCaml. This library allows applications to
access remote block devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make


%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install


%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/ipaddr
%exclude %{_libdir}/ocaml/ipaddr/*.a
%exclude %{_libdir}/ocaml/ipaddr/*.cmxa
%exclude %{_libdir}/ocaml/ipaddr/*.cmx
%exclude %{_libdir}/ocaml/ipaddr/*.ml
%exclude %{_libdir}/ocaml/ipaddr/*.mli


%files devel
%{_libdir}/ocaml/ipaddr/*.a
%{_libdir}/ocaml/ipaddr/*.cmx
%{_libdir}/ocaml/ipaddr/*.cmxa
%{_libdir}/ocaml/ipaddr/*.mli


%changelog
* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 2.4.0-1
- Initial package

