%global debug_package %{nil}

Name:           ocaml-cdrom
Version:        0.9.1
Release:        2%{?dist}
Summary:        Query the state of CDROM devices
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Libraries
URL:            http://github.com/xapi-project/cdrom
Source0:        https://github.com/xapi-project/cdrom/archive/cdrom-%{version}/cdrom-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-obuild
Requires:       ocaml ocaml-findlib

%description
Simple C bindings which allow the state of CDROM devices (and discs
inside) to be queried under Linux.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cdrom-cdrom-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml


%files
# This space intentionally left blank

%files devel
%doc ChangeLog README.md
%{_libdir}/ocaml/cdrom/*
%{_libdir}/ocaml/stublibs/dllstubs_cdrom.so
%{_libdir}/ocaml/stublibs/dllstubs_cdrom.so.owner

%changelog
* Tue May 28 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

