%define debug_package %{nil}

Name:           ocaml-biniou
Version:        1.0.6
Release:        1%{?dist}
Summary:        Compact, fast and extensible serialization format
License:        BSD3
Group:          Development/Libraries
URL:            http://mjambon.com/biniou.html
Source0:        http://mjambon.com/releases/biniou/biniou-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-findlib
Obsoletes:      biniou <= 1.0.6

%description
Binary data format designed for speed, safety, ease of use and backward
compatibility as protocols evolve.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
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
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}

%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md
%{_libdir}/ocaml/biniou/*
%{_bindir}/bdump

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.0.6-1
- Initial package

