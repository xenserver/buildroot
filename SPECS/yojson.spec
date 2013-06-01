Name:           ocaml-yojson
Version:        1.1.6
Release:        0
Summary:        A JSON parser and priter for OCaml
License:        BSD3
Group:          Development/Other
URL:            http://mjambon.com/releases/yojson/yojson-1.1.6.tar.gz
Source0:        yojson-1.1.6.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib cppo easy-format biniou
Requires:       ocaml ocaml-findlib

%description
A JSON parser and printer for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n yojson-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md LICENSE
%{_libdir}/ocaml/yojson/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

