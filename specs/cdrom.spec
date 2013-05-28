Name:           ocaml-cdrom
Version:        0.9.1
Release:        0
Summary:        Query the state of CDROM devices
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/xen-org/ocaml
Source0:        https://github.com/xen-org/cdrom/archive/cdrom-0.9.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Simple C bindings which allow the state of CDROM devices (and discs
inside) to be queried under Linux.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md
%{_libdir}/ocaml/cdrom/cdrom.a
%{_libdir}/ocaml/cdrom/cdrom.cma
%{_libdir}/ocaml/cdrom/cdrom.cmi
%{_libdir}/ocaml/cdrom/cdrom.cmxa
%{_libdir}/ocaml/cdrom/cdrom.mli
%{_libdir}/ocaml/cdrom/cdrom.cmx
%{_libdir}/ocaml/cdrom/cdrom.cmo
%{_libdir}/ocaml/cdrom/cdrom.o
%{_libdir}/ocaml/cdrom/cdrom_stubs.c.o
%{_libdir}/ocaml/cdrom/dllstubs_cdrom.so
%{_libdir}/ocaml/cdrom/libstubs_cdrom.a
%{_libdir}/ocaml/cdrom/META

%changelog
* Tue May 28 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

