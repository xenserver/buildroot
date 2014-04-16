%global debug_package %{nil}

Name:           ocaml-xenstore
Version:        1.2.4
Release:        1%{?dist}
Summary:        Xenstore protocol implementation in OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/mirage/ocaml-xenstore
Source0:        https://github.com/mirage/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ocamldoc
Requires:       ocaml
Requires:       ocaml-findlib
Conflicts:      xen-ocaml

%description
An implementation of the xenstore protocol in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Conflicts:      xen-ocaml-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install


%files
#This space intentionally left blank

%files devel
%doc README CHANGES LICENSE
%{_libdir}/ocaml/xenstore/*

%changelog
* Wed Sep 11 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.4-1
- Update to 1.2.4 (fixes critical watching bug)

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 1.2.3

* Sun May  2 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

