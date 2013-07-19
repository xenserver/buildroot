Name:           sm-cli
Version:        0.9.3
Release:        0
Summary:        CLI for xapi toolstack storage managers.
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/sm-cli/archive/sm-cli-%{version}.tar.gz
Source0:        https://github.com/xen-org/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-obuild ocaml-xcp-idl-devel cmdliner-devel ocaml-uuidm-devel
Requires:       message-switch

# XXX transitively required by message_switch
BuildRequires:  ocaml-oclock-devel

%description
Command-line interface for xapi toolstack storage managers.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/sm-cli/sm-cli %{buildroot}/%{_sbindir}/sm-cli

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/sm-cli

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

