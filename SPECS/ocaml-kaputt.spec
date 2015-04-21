%global debug_package %{nil}

Name:           ocaml-kaputt
Version:        1.2
Release:        1%{?dist}
Summary:        OCaml testing tool
License:        GPL
URL:            http://kaputt.x9c.fr/
Source0:        http://forge.ocamlcore.org/frs/download.php/987/kaputt-1.2.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
A unit testing tool for OCaml

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n kaputt-%{version}

%build
./configure
make all

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc COPYING
%doc README
%{_libdir}/ocaml/kaputt
%exclude %{_libdir}/ocaml/kaputt/*.a
%exclude %{_libdir}/ocaml/kaputt/*.cmxa
%exclude %{_libdir}/ocaml/kaputt/*.cmx

%files devel
%{_libdir}/ocaml/kaputt/*.a
%{_libdir}/ocaml/kaputt/*.cmx
%{_libdir}/ocaml/kaputt/*.cmxa

%changelog
* Sun Apr 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2-1
- Initial package


