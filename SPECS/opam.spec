Name:           opam
Version:        1.1.2
Release:        1%{?dist}
Summary:        Source-based OCaml package manager
License:        LGPLv3
URL:            http://opam.ocaml.org/
Source0:        https://github.com/ocaml/%{name}/releases/download/%{version}/%{name}-full-%{version}.tar.gz
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
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}/usr/man/* %{buildroot}/%{_mandir}
rm -rf %{buildroot}/usr/man

%files
%doc AUTHORS
%doc CHANGES
%doc CONTRIBUTING.md
%doc LICENSE
%doc README.md
%{_mandir}/man1/opam*
%{_bindir}/opam
%{_bindir}/opam-admin
%exclude %{_bindir}/opam-installer

%changelog
* Fri Aug 01 2014 Euan Harris <euan.harris@citrix.com> 1.1.2-1
- Initial package

