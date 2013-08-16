Name:           xe-create-templates
Version:        0.9.1
Release:        1
Summary:        Creates default XenServer templates
License:        LGPL
Group:          Development/Other
URL:            https://github.com/djs55/xcp-guest-templates/%{version}.tar.gz
Source0:        https://github.com/xapi-project/xcp-guest-templates/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel 
BuildRequires:  ocaml-lwt-devel xmlm-devel ocaml-stdext-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  openssl-devel
Requires:       openssl

%description
A utility to create the default XenServer templates.

%prep
%setup -q -n xcp-guest-templates-%{version}

%build
obuild configure
obuild build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 dist/build/xe-create-templates/xe-create-templates %{buildroot}/%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/xe-create-templates

%changelog
* Wed Jun 12 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

