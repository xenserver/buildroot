Name:           xenops-cli
Version:        0.10.0
Release:        1%{?dist}
Summary:        CLI for xenopsd, the xapi toolstack domain manager
License:        LGPL
URL:            https://github.com/xapi-project/xenops-cli
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel

%description
Command-line interface for xenopsd, the xapi toolstack domain manager.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install main.native %{buildroot}/%{_sbindir}/xenops-cli


%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xenops-cli

%changelog
* Thu Aug 20 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

