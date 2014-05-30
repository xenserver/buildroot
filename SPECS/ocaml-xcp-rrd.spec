%global debug_package %{nil}

Name:           ocaml-xcp-rrd
Version:        0.9.0
Release:        1%{?dist}
Summary:        Round-Robin Datasources in OCaml
License:        LGPL
URL:            https://github.com/xapi-project/xcp-rrd
Source0:        https://github.com/xapi-project/xcp-rrd/archive/xcp-rrd-%{version}/xcp-rrd-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel

%description
Round-Robin Datasources in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-rpc-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-rrd-xcp-rrd-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xcp-rrd/*

%changelog
* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

