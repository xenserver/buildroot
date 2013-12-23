%global debug_package %{nil}

Name:           ocaml-xenstore-clients
Version:        0.9.2
Release:        1
Summary:        Unix xenstore clients for OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/ocaml-xenstore-clients
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-lwt-devel ocaml-xenstore-devel
Requires:       ocaml ocaml-findlib

%description
Unix xenstore clients for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

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
#This space intentionally left blank

%files devel
%doc README.md LICENSE MAINTAINERS
%{_libdir}/ocaml/xenstore_transport/*

%changelog
* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

