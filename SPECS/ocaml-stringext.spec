Name:           ocaml-stringext
Version:        0.0.1
Release:        1%{?dist}
Summary:        String manipulation functions
License:        Unknown 
Group:          Development/Libraries
URL:            http://github.com/rgrinberg/stringext
Source0:        https://github.com/rgrinberg/stringext/archive/v%{version}/stringext-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
Extra string functions for OCaml

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n stringext-%{version}


%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%files
%{_libdir}/ocaml/stringext
%exclude %{_libdir}/ocaml/stringext/*.a
%exclude %{_libdir}/ocaml/stringext/*.cmxa
%exclude %{_libdir}/ocaml/stringext/*.cmx
%exclude %{_libdir}/ocaml/stringext/*.mli


%files devel
%{_libdir}/ocaml/stringext/*.a
%{_libdir}/ocaml/stringext/*.cmx
%{_libdir}/ocaml/stringext/*.cmxa
%{_libdir}/ocaml/stringext/*.mli

%changelog
* Fri May 2 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.0.1-1
- Initial package

