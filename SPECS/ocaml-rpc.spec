%global debug_package %{nil}

Name:           ocaml-rpc
Version:        1.5.0
Release:        1%{?dist}
Summary:        An RPC library for OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/samoht/ocaml-rpc
Source0:        https://github.com/samoht/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         ocaml-rpc-no-js.patch
Patch1:         ocaml-rpc-no-js2.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-type-conv
BuildRequires:  xmlm-devel

%description
Am RPC library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-camlp4-devel%{?_isa}
Requires:       ocaml-type-conv%{?_isa}
Requires:       xmlm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
* Mon May 12 2014 David Scott <dave.scott@citrix.com> - 1.5.0-1
* Update to 1.5.0

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.4.1-1
- Initial package

