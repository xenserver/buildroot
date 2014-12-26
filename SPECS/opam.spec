Name:           opam
Version:        1.2.0
Release:        1%{?dist}
Summary:        Source-based OCaml package manager
License:        LGPLv3
URL:            http://opam.ocaml.org/
Source0:        https://github.com/ocaml/%{name}/releases/download/%{version}/%{name}-full-%{version}.tar.gz
BuildRequires:  curl 
BuildRequires:  ocaml 

%description
Source-based OCaml package manager

%prep
%setup -q -n %{name}-full-%{version}

%build
%configure
make lib-ext
make

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS
%doc CHANGES
%doc CONTRIBUTING.md
%doc LICENSE
%doc README.md
%{_bindir}/opam
%{_bindir}/opam-admin
%{_bindir}/opam-installer

%changelog
* Fri Dec 26 2014 David Scott <dave.scott@citrix.com> - 1.2.0-1
- Update to 1.2.0

* Fri Aug 01 2014 Euan Harris <euan.harris@citrix.com> - 1.1.2-1
- Initial package

