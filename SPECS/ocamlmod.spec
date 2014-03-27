Name:		ocamlmod
Version:	0.0.7
Release:	1%{?dist}
Summary:	Generate OCaml modules from source files

Group:		Development/Tools
License:	LGPL
URL:		http://forge.ocamlcore.org/projects/ocamlmod/
Source0:	http://forge.ocamlcore.org/frs/download.php/1350/%{name}-%{version}.tar.gz

BuildRequires:	ocaml >= 3.10.2
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-ounit-devel >= 2.0.0

Requires:	ocaml

%description


%prep
%setup -q


%build
ocaml setup.ml -configure --prefix %{_prefix} --destdir %{buildroot}
ocaml setup.ml -build

%install
ocaml setup.ml -install


%files
%doc AUTHORS.txt CHANGES.txt
%{_bindir}/ocamlmod


%changelog
* Tue Mar 25 2014 Euan Harris <euan.harris@citrix.com> - 0.0.7-1
- Initial package

