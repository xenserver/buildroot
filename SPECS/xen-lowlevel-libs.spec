Name:           ocaml-xen-lowlevel-libs
Version:        0.9.0
Release:        1
Summary:        Xen hypercall bindings for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/ocaml-xen-lowlevel-libs/archive/ocaml-xen-lowlevel-libs-0.9.0.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel ocaml-lwt-devel xen-devel
Requires:       ocaml ocaml-findlib

%description
Xen hypercall bindings for OCaml.

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
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md
%{_libdir}/ocaml/xenctrl/*
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so.owner

%changelog
* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

