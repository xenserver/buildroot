%global debug_package %{nil}

Name:           ocaml-xcp-rrd
Version:        0.9.0
Release:        2%{?dist}
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
BuildRequires:  ocaml-uuidm-devel

%description
Round-Robin Datasources in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-rpc-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}
Requires:       ocaml-uuidm-devel%{?_isa}

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
%doc ChangeLog 
%doc LICENSE 
%doc MAINTAINERS
%doc README.md 
%{_libdir}/ocaml/xcp-rrd
%exclude %{_libdir}/ocaml/xcp-rrd/*.a
%exclude %{_libdir}/ocaml/xcp-rrd/*.cmxa
%exclude %{_libdir}/ocaml/xcp-rrd/*.cmx

%files devel
%{_libdir}/ocaml/xcp-rrd/*.a
%{_libdir}/ocaml/xcp-rrd/*.cmxa
%{_libdir}/ocaml/xcp-rrd/*.cmx

%changelog
* Mon Jun  2 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Split files correctly between base and devel packages

* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

