Name:           ocaml-xenstore-clients
Version:        0.9.0
Release:        0
Summary:        Unix xenstore clients for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/ocaml-xenstore-clients/archive/ocaml-xenstore-clients-%{version}.tar.gz
Source0:        https://github.com/xen-org/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-lwt-devel ocaml-xenstore-devel
Requires:       ocaml ocaml-findlib

%description
Unix xenstore clients for OCaml.

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
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_libdir}/ocaml/xenstore_transport/*

%changelog
* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

