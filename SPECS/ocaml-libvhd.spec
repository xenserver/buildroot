%global debug_package %{nil}

Name:           ocaml-libvhd
Version:        0.9.1
Release:        1%{?dist}
Summary:        VHD manipulation via libvhd
License:        BSD3
Group:          Development/Libraries
URL:            http://github.com/xapi-project/libvhd
Source0:        https://github.com/xapi-project/libvhd/archive/libvhd-%{version}/libvhd-%{version}.tar.gz
BuildRequires:  libuuid-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  xen-devel

%description
Simple C bindings which allow .vhd files to be manipulated.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libuuid-devel%{?_isa}
Requires:       xen-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n libvhd-libvhd-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%doc ChangeLog README.md
%{_libdir}/ocaml/vhdlib/*
%{_libdir}/ocaml/stublibs/dllvhdlib_stubs.so
%{_libdir}/ocaml/stublibs/dllvhdlib_stubs.so.owner

%changelog
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Initial package

