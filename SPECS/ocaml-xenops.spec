Name:           ocaml-xenops
Version:        0.9.0
Release:        0
Summary:        Low-level xen control operations OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xenops/archive/xenops-%{version}.tar.gz
Source0:        https://github.com/xen-org/xenops/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-obuild ocaml-stdext-devel ocaml-rpc-devel ocaml-camlp4-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel ocaml-xenstore-devel ocaml-xenstore-clients-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
Requires:       ocaml ocaml-findlib

%description
Low-level xen control operations in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xenops-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xenops/*

%changelog
* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

