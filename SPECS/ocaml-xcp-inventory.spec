%global debug_package %{nil}

Name:           ocaml-xcp-inventory
Version:        0.9.0
Release:        1
Summary:        OCaml library to read and write the XCP inventory file
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/xapi-project/xcp-inventory
Source0:        https://github.com/xapi-project/xcp-inventory/archive/xcp-inventory-%{version}/xcp-inventory-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib-devel ocaml-obuild cmdliner-devel ocaml-uuidm-devel ocaml-stdext-devel

%description
A simple library to read and write the XCP inventory file.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       ocaml ocaml-findlib

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-inventory-xcp-inventory-%{version}

%build
if [ -x ./configure ]; then
  ./configure --default_inventory=/etc/xcp/inventory
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/etc/xcp

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/xcp

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md LICENSE

%{_libdir}/ocaml/xcp-inventory/*

%changelog
* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

