%global debug_package %{nil}

Name:           ocaml-xenops
Version:        0.9.4
Release:        1%{?dist}
Summary:        Low-level xen control operations OCaml
License:        LGPL
URL:            https://github.com/xapi-project/xenops
Source0:        https://github.com/xapi-project/xenops/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel

%description
Low-level xen control operations in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-xcp-idl-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}
Requires:       ocaml-xen-lowlevel-libs-devel%{?_isa}
Requires:       ocaml-xenstore-devel%{?_isa}
Requires:       ocaml-xenstore-clients-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        tools
Summary:        Debugging tools for %{name}
Requires:       xen-libs
BuildRequires:  xen-devel

%description   tools
A set of debugging tools which showcase the features of %{name}-devel.

%prep
%setup -q -n xenops-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xenops/*

%files tools
%{_bindir}/list_domains

%changelog
* Thu May  8 2014 David Scott <dave.scott@citrix.com> - 0.9.4-1
- Update to 0.9.4, add list_domains binary

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

