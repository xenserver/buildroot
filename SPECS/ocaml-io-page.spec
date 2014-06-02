%define debug_package %{nil}

Name:           ocaml-io-page
Version:        1.1.1
Release:        2%{?dist}
Summary:        Efficient handling of I/O memory pages on Unix and Xen.
License:        ISC
URL:            https://github.com/mirage/io-page
Source0:        https://github.com/mirage/io-page/archive/v%{version}/io-page-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit-devel

%description
This library implements support for efficient handling of I/O memory pages on Unix and Xen.

IO pages are page-aligned, and wrapped in the Cstruct library to avoid copying the data contained within the page.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n io-page-%{version}

%build
./configure --destdir %{buildroot}%{_libdir}/ocaml
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%doc CHANGES 
%doc README.md
%{_libdir}/ocaml/io-page
%exclude %{_libdir}/ocaml/io-page/*.a
%exclude %{_libdir}/ocaml/io-page/*.cmxa
%exclude %{_libdir}/ocaml/io-page/*.cmx
%exclude %{_libdir}/ocaml/io-page/*.mli

%files devel
%{_libdir}/ocaml/io-page/*.a
%{_libdir}/ocaml/io-page/*.cmx
%{_libdir}/ocaml/io-page/*.cmxa
%{_libdir}/ocaml/io-page/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-2
- Split files corrrectly between base and devel packages

* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-1
- Initial package

