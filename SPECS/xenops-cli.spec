Name:           xenops-cli
Version:        0.9.1
Release:        1
Summary:        CLI for xenopsd, the xapi toolstack domain manager
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xenops-cli/archive/xenops-cli-%{version}.tar.gz
Source0:        https://github.com/xen-org/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-obuild ocaml-xcp-idl-devel cmdliner-devel ocaml-uuidm-devel
Requires:       message-switch

# XXX transitively required by message_switch
BuildRequires:  ocaml-oclock-devel

%description
Command-line interface for xenopsd, the xapi toolstack domain manager.

%prep
%setup -q -n xenops-cli-xenops-cli-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install main.native %{buildroot}/%{_sbindir}/xenops-cli

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xenops-cli

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

