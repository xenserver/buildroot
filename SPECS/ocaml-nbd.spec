%global debug_package %{nil}

Name:           ocaml-nbd
Version:        0.9.1
Release:        1
Summary:        Pure OCaml implementation of the Network Block Device protocol
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/djs55/nbd
Source0:        https://github.com/djs55/nbd/archive/%{version}/nbd-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-bitstring-devel ocaml-lwt-devel ocaml-obuild ocaml-camlp4-devel ocaml-camlp4
Requires:       ocaml ocaml-findlib

%description
An implementation of the Network Block Device protocol for both
regular Unix and Lwt in OCaml. This library allows applications to
access remote block devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n nbd-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc ChangeLog README.markdown

%{_libdir}/ocaml/nbd/nbd_lwt.a
%{_libdir}/ocaml/nbd/nbd_lwt.cmxa
%{_libdir}/ocaml/nbd/nbd_lwt_common.cmo
%{_libdir}/ocaml/nbd/nbd_lwt_server.cmi
%{_libdir}/ocaml/nbd/nbd_lwt_client.cmx
%{_libdir}/ocaml/nbd/nbd_lwt_common.cmt
%{_libdir}/ocaml/nbd/lwt_mux.cmx
%{_libdir}/ocaml/nbd/lwt_mux.cmt
%{_libdir}/ocaml/nbd/lwt_mux.cmo
%{_libdir}/ocaml/nbd/nbd_lwt.cma
%{_libdir}/ocaml/nbd/lwt_mux.cmi
%{_libdir}/ocaml/nbd/nbd_lwt_client.cmt
%{_libdir}/ocaml/nbd/nbd_lwt_server.cmo
%{_libdir}/ocaml/nbd/nbd_lwt_client.o
%{_libdir}/ocaml/nbd/nbd_lwt_server.o
%{_libdir}/ocaml/nbd/lwt_mux.o
%{_libdir}/ocaml/nbd/nbd_lwt_common.cmi
%{_libdir}/ocaml/nbd/nbd_lwt_client.cmo
%{_libdir}/ocaml/nbd/nbd_lwt_common.cmti
%{_libdir}/ocaml/nbd/nbd_lwt_client.cmi
%{_libdir}/ocaml/nbd/nbd_lwt_common.cmx
%{_libdir}/ocaml/nbd/nbd_lwt_common.o
%{_libdir}/ocaml/nbd/nbd_lwt_client.cmti
%{_libdir}/ocaml/nbd/nbd_lwt_server.cmti
%{_libdir}/ocaml/nbd/nbd_lwt_server.cmx
%{_libdir}/ocaml/nbd/nbd_lwt_server.cmt
%{_libdir}/ocaml/nbd/result.cmi
%{_libdir}/ocaml/nbd/nbd.a
%{_libdir}/ocaml/nbd/nbd.cmt
%{_libdir}/ocaml/nbd/nbd.o
%{_libdir}/ocaml/nbd/nbd.cmti
%{_libdir}/ocaml/nbd/nbd.cmo
%{_libdir}/ocaml/nbd/result.cmt
%{_libdir}/ocaml/nbd/nbd.cmxa
%{_libdir}/ocaml/nbd/nbd.cmx
%{_libdir}/ocaml/nbd/result.cmo
%{_libdir}/ocaml/nbd/result.o
%{_libdir}/ocaml/nbd/result.cmx
%{_libdir}/ocaml/nbd/nbd.cmi
%{_libdir}/ocaml/nbd/nbd.cma
%{_libdir}/ocaml/nbd/META

%changelog
* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

