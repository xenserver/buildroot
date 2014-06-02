%global debug_package %{nil}

Name:           ocaml-zed
Version:        1.2
Release:        2%{?dist}
Summary:        An abstract engine for text editing for OCaml
License:        BSD3
URL:            http://forge.ocamlcore.org/projects/zed/
Source0:        http://forge.ocamlcore.org/frs/download.php/944/zed-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camomile-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-react-devel

%description
Zed is an abstract engine for text editing. It can be used for writing
text editors, editing widgets, readlines...

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-camomile-devel%{?_isa}
Requires:       ocaml-react-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n zed-%{version}

%build
./configure --destdir %{buildroot}/%{_libdir}/ocaml
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc LICENSE
%{_libdir}/ocaml/zed
%exclude %{_libdir}/ocaml/zed/*.a
%exclude %{_libdir}/ocaml/zed/*.cmxa
%exclude %{_libdir}/ocaml/zed/*.cmx
%exclude %{_libdir}/ocaml/zed/*.mli

%files devel
%{_libdir}/ocaml/zed/*.a
%{_libdir}/ocaml/zed/*.cmxa
%{_libdir}/ocaml/zed/*.cmx
%{_libdir}/ocaml/zed/*.mli

%changelog
* Mon Jun  2 2014 Euan Harris <euan.harris@citrix.com> - 1.2-2
- Split files correctly between base and devel packages

* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com> - 1.2-1
- Initial package

