%global debug_package %{nil}

Name:           ocaml-zed
Version:        1.2
Release:        1
Summary:        An abstract engine for text editing for OCaml
License:        BSD3
Group:          Development/Libraries
URL:            http://forge.ocamlcore.org/projects/zed/
Source0:        http://forge.ocamlcore.org/frs/download.php/944/zed-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc ocaml-camomile-devel ocaml-react-devel
Requires:       ocaml ocaml-findlib

%description
Zed is an abstract engine for text edition. It can be used for writing
text editors, edition widgets, readlines, ...

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n zed-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
#This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc LICENSE CHANGES
%{_libdir}/ocaml/zed/*

%changelog
* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

