Name:           ocaml-stdext
Version:        0.9.0
Release:        0
Summary:        Deprecated misc library functions for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/stdext/archive/stdext-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-fd-send-recv-devel ocaml-uuidm-devel
Requires:       ocaml ocaml-findlib

%description
Deprecated misc library functions for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n stdext-stdext-%{version}

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
%doc README.md
%{_libdir}/ocaml/stdext/*

%changelog
* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

