%define debug_package %{nil}

Name:           ocaml-biniou
Version:        1.0.6
Release:        3%{?dist}
Summary:        Compact, fast and extensible serialization format
License:        BSD3
URL:            http://mjambon.com/biniou.html
Source0:        https://github.com/mjambon/biniou/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-findlib
Obsoletes:      biniou <= 1.0.6

%description
Binary data format designed for speed, safety, ease of use and backward
compatibility as protocols evolve.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-easy-format-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n biniou-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}

%files
%doc LICENSE
%doc README.md
%{_bindir}/bdump
%{_libdir}/ocaml/biniou
%exclude %{_libdir}/ocaml/biniou/*.a
%exclude %{_libdir}/ocaml/biniou/*.cmxa
%exclude %{_libdir}/ocaml/biniou/*.cmx
%exclude %{_libdir}/ocaml/biniou/*.mli

%files devel
%{_libdir}/ocaml/biniou/*.a
%{_libdir}/ocaml/biniou/*.cmx
%{_libdir}/ocaml/biniou/*.cmxa
%{_libdir}/ocaml/biniou/*.mli

%changelog
* Tue Oct 21 2014 Euan Harris <euan.harris@citrix.com> - 1.0.6-3
- Switch to GitHub sources

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.0.6-2
- Split files correctly between base and devel packages

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.0.6-1
- Initial package

