Name:           xe-create-templates
Version:        0.9.2
Release:        1%{?dist}
Summary:        Creates default XenServer templates
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xcp-guest-templates
Source0:        https://github.com/xapi-project/xcp-guest-templates/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xmlm-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel

%description
A utility to create the default XenServer templates.

%prep
%setup -q -n xcp-guest-templates-%{version}

%build
obuild configure
obuild build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 dist/build/xe-create-templates/xe-create-templates %{buildroot}/%{_bindir}/


%files
%doc README.md
%{_bindir}/xe-create-templates

%changelog
* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Wed Jun 12 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

