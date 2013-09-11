%global debug_package %{nil}

Name:           ocaml-rpc
Version:        1.4.1
Release:        1
Summary:        An RPC library for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/samoht/ocaml-rpc/archive/1.4.1.tar.gz
Source0:        https://github.com/samoht/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-type-conv xmlm-devel js_of_ocaml-devel ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib ocaml-type-conv ocaml-camlp4-devel

%description
Am RPC library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc README.md
%{_libdir}/ocaml/rpclib/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

