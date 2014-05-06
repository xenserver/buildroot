Name:           xenops-cli
Version:        0.9.1
Release:        2%{?dist}
Summary:        CLI for xenopsd, the xapi toolstack domain manager
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xenops-cli
Source0:        https://github.com/xapi-project/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel

%description
Command-line interface for xenopsd, the xapi toolstack domain manager.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install main.native %{buildroot}/%{_sbindir}/xenops-cli


%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xenops-cli

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

