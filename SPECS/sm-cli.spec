Name:           sm-cli
Version:        0.9.4
Release:        1
Summary:        CLI for xapi toolstack storage managers
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/sm-cli
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-obuild ocaml-xcp-idl-devel cmdliner-devel ocaml-uuidm-devel
BuildRequires:  message-switch-devel
Requires:       message-switch

# XXX transitively required by message_switch
BuildRequires:  ocaml-oclock-devel

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
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/sm-cli

%changelog
* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update to 0.9.4

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

