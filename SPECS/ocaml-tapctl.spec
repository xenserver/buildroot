%global debug_package %{nil}

Name:           ocaml-tapctl
Version:        0.9.1
Release:        1
Summary:        Manipulate running tapdisk instances
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/tapctl/archive/%{version}.tar.gz
Source0:        https://github.com/xapi-project/tapctl/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  forkexecd-devel ocaml-stdext-devel ocaml-rpc-devel ocaml-xcp-idl-devel ocaml-oclock-devel
Requires:       ocaml ocaml-findlib forkexecd-devel

%description
Manipulate running tapdisk instances on a xen host.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n tapctl-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
#This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/tapctl/*

%changelog
* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

