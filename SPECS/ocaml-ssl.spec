%global debug_package %{nil}

Name:           ocaml-ssl
Version:        0.4.6
Release:        1
Summary:        Use OpenSSL from OCaml
License:        LGPL
Group:          Development/Libraries
URL:            http://downloads.sourceforge.net/project/savonet/ocaml-ssl
Source0:        http://downloads.sourceforge.net/project/savonet/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib openssl-devel
Requires:       ocaml ocaml-findlib openssl

%description
Use OpenSSL from OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
# --disable-ldconf
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}


%files
#This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc CHANGES COPYING README
%{_libdir}/ocaml/ssl/*
%{_libdir}/ocaml/stublibs/dllssl_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_stubs.so.owner

%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so.owner

%changelog
* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com> - 0.4.6-1
- Initial package

