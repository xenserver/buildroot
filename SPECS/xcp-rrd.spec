Name:           ocaml-xcp-rrd
Version:        0.9.0
Release:        0
Summary:        Round-Robin Datasources in OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xcp-rrd/archive/xcp-rrd-%{version}.tar.gz
Source0:        https://github.com/xen-org/xcp-rrd/archive/xcp-rrd-%{version}/xcp-rrd-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-obuild ocaml-stdext-devel ocaml-rpc-devel ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib

%description
Round-Robin Datasources in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-rrd-xcp-rrd-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xcp-rrd/*

%changelog
* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

