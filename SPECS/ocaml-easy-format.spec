Name:           ocaml-easy-format
Version:        1.0.1
Release:        2%{?dist}
Summary:        Indentation made easy
License:        BSD3
URL:            http://mjambon.com/easy-format.html
Source0:        http://mjambon.com/releases/easy-format/easy-format-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
Obsoletes:      easy-format <= 1.0.1

%description
Easy_format: indentation made easy.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n easy-format-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc LICENSE
%doc README
%{_libdir}/ocaml/easy-format
%exclude %{_libdir}/ocaml/easy-format/*.cmx
%exclude %{_libdir}/ocaml/easy-format/*.mli

%files devel
%{_libdir}/ocaml/easy-format/*.cmx
%{_libdir}/ocaml/easy-format/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.0.1-2
- Split files correctly between base and devel packages

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.0.1-1
- Initial package

