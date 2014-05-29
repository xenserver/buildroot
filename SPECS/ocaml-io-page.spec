%define debug_package %{nil}

Name:           ocaml-io-page
Version:        1.1.1
Release:        1%{?dist}
Summary:        Efficient handling of I/O memory pages on Unix and Xen.
License:        ISC
URL:            https://github.com/mirage/io-page
Source0:        http://github.com/mirage/io-page/archive/v%{version}/io-page-%{version}.tar.gz
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
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/ocaml/io-page/META
%{_libdir}/ocaml/io-page/io_page.cma
%{_libdir}/ocaml/io-page/io_page.cmi
%{_libdir}/ocaml/io-page/dllio_page_unix_stubs.so

%files devel
%defattr(-,root,root)
%doc CHANGES README.md
%{_libdir}/ocaml/io-page/io_page.a
%{_libdir}/ocaml/io-page/io_page.cmx
%{_libdir}/ocaml/io-page/io_page.cmxa
%{_libdir}/ocaml/io-page/io_page.cmxs
%{_libdir}/ocaml/io-page/io_page.mli
%{_libdir}/ocaml/io-page/libio_page_unix_stubs.a
%{_libdir}/ocaml/io-page/io_page_unix.a
%{_libdir}/ocaml/io-page/io_page_unix.cma
%{_libdir}/ocaml/io-page/io_page_unix.cmi
%{_libdir}/ocaml/io-page/io_page_unix.cmx
%{_libdir}/ocaml/io-page/io_page_unix.cmxa
%{_libdir}/ocaml/io-page/io_page_unix.cmxs
%{_libdir}/ocaml/io-page/io_page_unix.ml

%changelog
* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-1
- Initial package
