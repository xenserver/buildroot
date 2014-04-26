# -*- rpm-spec -*-

Summary: Command-line tools for controlling xapi
Name:    xe
Version: 0.6.2
Release: 1%{?dist}
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  https://github.com/djs55/xapi-xe
Source0: https://github.com/djs55/xapi-xe/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-cstruct-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-ssl-devel
BuildRequires: openssl-devel
BuildRequires: ocaml-uuidm-devel
BuildRequires: ocaml-uri-devel
BuildRequires: ocaml-cohttp-devel >= 0.10.0
BuildRequires: ocaml-re-devel

Provides: xapi-xe

%description
Simple command-line tool for controlling xapi.

%prep 
%setup -q -n xapi-xe-%{version}

%build
make

%install
 
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}
mkdir -p %{buildroot}/etc/bash-completion.d
cp src/bash-completion/xe %{buildroot}/etc/bash-completion.d

%files
%{_bindir}/xe
/etc/bash-completion.d/xe

%changelog
* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 0.6.2-2
- Initial package
