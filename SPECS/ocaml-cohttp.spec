%global debug_package %{nil}

Name:           ocaml-cohttp
Version:        0.9.8
Release:        1
Summary:        An HTTP library for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8.tar.gz
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-re-devel ocaml-uri-devel ocaml-cstruct-devel ocaml-lwt-devel ocaml-ounit-devel ocaml-ocamldoc ocaml-camlp4-devel
# should these be inherited from ssl.spec somehow?
BuildRequires:  openssl openssl-devel
Requires:       ocaml ocaml-findlib

%description
An HTTP library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
make build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc LICENSE README.md CHANGES
%{_libdir}/ocaml/cohttp/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

