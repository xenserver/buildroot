%global debug_package %{nil}

Name:           ocaml-xcp-inventory
Version:        0.9.1
Release:        1%{?dist}
Summary:        OCaml library to read and write the XCP inventory file
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/xcp-inventory
Source0:        https://github.com/xapi-project/xcp-inventory/archive/v%{version}/xcp-inventory-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-uuidm-devel

%description
A simple library to read and write the XCP inventory file.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-stdext-devel%{?_isa}
Requires:       ocaml-uuidm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-inventory-%{version}

%build
if [ -x ./configure ]; then
  ./configure --default_inventory=/etc/xcp/inventory
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/etc/xcp


%files
/etc/xcp

%files devel
%doc ChangeLog README.md LICENSE

%{_libdir}/ocaml/xcp-inventory/*

%changelog
* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-1
- Update to 0.9.1

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

