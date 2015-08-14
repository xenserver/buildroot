Name:           sm-cli
Version:        0.9.5
Release:        1%{?dist}
Summary:        CLI for xapi toolstack storage managers
License:        LGPL
URL:            https://github.com/xapi-project/sm-cli
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel

%description
Command-line interface for xapi toolstack storage managers.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/sm-cli/sm-cli %{buildroot}/%{_sbindir}/sm-cli


%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/sm-cli

%changelog
* Fri Aug 14 2015 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update to 0.9.4

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

