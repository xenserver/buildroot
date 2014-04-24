Name:           ocaml-easy-format
Version:        1.0.1
Release:        1%{?dist}
Summary:        Indentation made easy
License:        BSD3
Group:          Development/Libraries
URL:            http://mjambon.com/easy-format.html
Source0:        http://mjambon.com/releases/easy-format/easy-format-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
Obsoletes:      easy-format <= 1.0.1

%description
Easy_format: indentation made easy.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n easy-format-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%files
#This space intentionally left blank

%files devel
%doc LICENSE README
%{_libdir}/ocaml/easy-format/*

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.0.1-1
- Initial package

