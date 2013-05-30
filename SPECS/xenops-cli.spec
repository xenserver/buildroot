Name:           xenops-cli
Version:        0.9.0
Release:        0
Summary:        CLI for xenopsd, the xapi toolstack domain manager
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/xenops-cli/archive/xenops-cli-0.9.0.tar.gz
Source0:        xenops-cli-0.9.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
Requires:       ocaml

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

