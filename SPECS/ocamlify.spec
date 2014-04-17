Name:		ocamlify
Version:	0.0.2
Release:	1%{?dist}
Summary:	Create OCaml source code by including whole files into OCaml string or string list
Group:		Development/Tools
License:	LGPL
URL:		http://forge.ocamlcore.org/projects/ocamlify/
Source0:	http://forge.ocamlcore.org/frs/download.php/1209/%{name}-%{version}.tar.gz


BuildRequires:	ocaml >= 3.10.2
BuildRequires:	ocaml-findlib-devel


%description
Create OCaml source code by including whole files into OCaml string or
string list.


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
%doc COPYING.txt 
%{_bindir}/ocamlify


%changelog
* Tue Mar 25 2014 Euan Harris <euan.harris@citrix.com> - 0.0.2-1
- Initial package

