Name:		ocamlmod
Version:	0.0.7
Release:	1%{?dist}
Summary:	Generate OCaml modules from source files
License:	LGPL
URL:		http://forge.ocamlcore.org/projects/ocamlmod/
Source0:	http://forge.ocamlcore.org/frs/download.php/1350/%{name}-%{version}.tar.gz


BuildRequires:	ocaml >= 3.10.2
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-ounit-devel >= 2.0.0


%description
Generate OCaml modules from source files.


%prep
%setup -q


%build
./configure --prefix %{_prefix} --destdir %{buildroot}
make


%install
make install


%files
%doc AUTHORS.txt 
%doc CHANGES.txt
%{_bindir}/ocamlmod


%changelog
* Tue Mar 25 2014 Euan Harris <euan.harris@citrix.com> - 0.0.7-1
- Initial package

