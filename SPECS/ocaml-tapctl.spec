%global debug_package %{nil}

Name:           ocaml-tapctl
Version:        0.9.1
Release:        1%{?dist}
Summary:        Manipulate running tapdisk instances
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/tapctl
Source0:        https://github.com/xapi-project/tapctl/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xcp-idl-devel

%description
Manipulate running tapdisk instances on a xen host.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n tapctl-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/tapctl/*

%changelog
* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

