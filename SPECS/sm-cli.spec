Name:           sm-cli
Version:        0.9.0
Release:        0
Summary:        CLI for xapi toolstack storage managers.
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/sm-cli/archive/sm-cli-0.9.0.tar.gz
Source0:        sm-cli-0.9.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
Requires:       ocaml

%description
Command-line interface for xapi toolstack storage managers.

%prep
%setup -q -n sm-cli-sm-cli-%{version}

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

