Name:           ocaml-libvhd
Version:        0.9.1
Release:        0
Summary:        vhd manipulation via libvhd
License:        BSD3
Group:          Development/Other
URL:            http://github.com/xen-org/libvhd
Source0:        https://github.com/xen-org/libvhd/archive/libvhd-%{version}/libvhd-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib xen-devel libuuid-devel
Requires:       ocaml ocaml-findlib

%description
Simple C bindings which allow .vhd files to be manipulated.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n libvhd-libvhd-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md
%{_libdir}/ocaml/vhdlib/*
%{_libdir}/ocaml/stublibs/dllvhdlib_stubs.so
%{_libdir}/ocaml/stublibs/dllvhdlib_stubs.so.owner

%changelog
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

