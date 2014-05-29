%global debug_package %{nil}

Name:           ocaml-rpc
Version:        1.5.1
Release:        1%{?dist}
Summary:        An RPC library for OCaml
License:        LGPL
URL:            https://github.com/samoht/ocaml-rpc
Source0:        https://github.com/samoht/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-type-conv
BuildRequires:  ocaml-xmlm-devel

%description
Am RPC library for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-camlp4-devel%{?_isa}
Requires:       ocaml-type-conv%{?_isa}
Requires:       ocaml-lwt%{?_isa}
Requires:       ocaml-xmlm-devel%{?_isa}

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
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%files
%doc README.md
%{_libdir}/ocaml/rpclib
%exclude %{_libdir}/ocaml/rpclib/*.cmx

%files devel
%{_libdir}/ocaml/rpclib/*.cmx

%changelog
* Fri May 23 2014 Euan Harris <euan.harris@citrix.com> - 1.5.1-1
- Update to 1.5.1, removing dependency on js-of-ocaml

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.4.1-1
- Initial package

