Name:           ocaml-ssl
Version:        0.4.6
Release:        1
Summary:        Use OpenSSL from OCaml
License:        LGPL
Group:          Development/Other
URL:            http://downloads.sourceforge.net/project/savonet/ocaml-ssl/0.4.6/ocaml-ssl-0.4.6.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib openssl-devel
Requires:       ocaml ocaml-findlib openssl

%description
Use OpenSSL from OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-ssl-%{version}

%build
./configure
# --disable-ldconf
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc CHANGES COPYING README
%{_libdir}/ocaml/ssl/*
%{_libdir}/ocaml/stublibs/dllssl_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_stubs.so.owner

%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so.owner

%changelog
* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

