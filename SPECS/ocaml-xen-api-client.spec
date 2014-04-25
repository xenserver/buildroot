%global debug_package %{nil}

Name:           ocaml-xen-api-client
Version:        0.9.4
Release:        1%{?dist}
Summary:        XenServer XenAPI Client Library for OCaml
License:        LGPLv2
Group:          Development/Libraries
URL:            https://github.com/xapi-project/xen-api-client
Source0:        https://github.com/xapi-project/xen-api-client/archive/%{version}/xen-api-client-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-ssl-devel
BuildRequires:  ocaml-uri-devel
BuildRequires:  openssl-devel
BuildRequires:  xmlm-devel

%description
XenAPI Client is an OCaml library implementing XenServer's XenAPI.
It is used for programmatically controlling a pool of XenServer
virtualization hosts.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
XenAPI Client is an OCaml library implementing XenServer's XenAPI.
It is used for programmatically controlling a pool of XenServer
virtualization hosts.

%prep
%setup -q -n xen-api-client-%{version}

%build
ocaml setup.ml -configure --disable-tests --enable-lwt
ocaml setup.ml -build
ocaml setup.ml -doc

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml ocaml setup.ml -install


%files
#This space intentionally left blank

%files devel
%doc README.md CHANGES
%{_libdir}/ocaml/xen-api-client/*


%changelog
* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update to 0.9.3

* Wed May 29 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package
