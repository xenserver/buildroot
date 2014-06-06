Name:           ocaml-conduit
Version:        0.5.0
Release:        1%{?dist}
Summary:        OCaml network conduit library
License:        Unknown 
Group:          Development/Libraries
URL:            https://github.com/mirage/ocaml-conduit
Source0:        https://github.com/mirage/ocaml-conduit/archive/v%{version}/ocaml-conduit-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-lwt-devel

%description
The conduit library takes care of establishing and listening for TCP and SSL/TLS connections for the Lwt and Async libraries.

The reason this library exists is to provide a degree of abstraction from the precise SSL library used, since there are a variety of ways to bind to a library (e.g. the C FFI, or the Ctypes library), as well as well as which library is used (just OpenSSL for now).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q


%build
make all

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%{_libdir}/ocaml/conduit
%exclude %{_libdir}/ocaml/conduit/*.a
%exclude %{_libdir}/ocaml/conduit/*.cmxa
%exclude %{_libdir}/ocaml/conduit/*.cmx


%files devel
%{_libdir}/ocaml/conduit/*.a
%{_libdir}/ocaml/conduit/*.cmx
%{_libdir}/ocaml/conduit/*.cmxa

%changelog
* Fri May 2 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.5.0-1
- Initial package

