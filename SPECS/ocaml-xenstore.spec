%global debug_package %{nil}

Name:           ocaml-xenstore
Version:        1.2.4
Release:        1
Summary:        Xenstore protocol implementation in OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/mirage/ocaml-xenstore
Source0:        https://github.com/mirage/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-cstruct-devel ocaml-lwt-devel ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
Requires:       ocaml ocaml-findlib
Conflicts:      xen-ocaml

%description
An implementation of the xenstore protocol in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
#This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc README CHANGES LICENSE
%{_libdir}/ocaml/xenstore/*

%changelog
* Wed Sep 11 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 1.2.4 (fixes critical watching bug)

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 1.2.3

* Sun May  2 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

