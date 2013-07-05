Name:           ocaml-xen-api-client
Version:        0.9.4
Release:        0
Summary:        XenServer XenAPI Client Library for OCaml
License:        LGPLv2
Group:          Development/Libraries
URL:            https://github.com/xen-org/xen-api-client
Source0:        https://github.com/xen-org/xen-api-client/archive/%{version}/xen-api-client-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel ocaml-lwt-devel ocaml-ssl-devel openssl openssl-devel ocaml-ounit-devel ocaml-cohttp-devel ocaml-uri-devel xmlm-devel ocaml-rpc-devel
Requires:       ocaml ocaml-findlib

%description
XenAPI Client is an OCaml library implementing XenServer's XenAPI.
It is used for programmatically controlling a pool of XenServer
virtualization hosts.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md CHANGES
%{_libdir}/ocaml/xen-api-client/*


%changelog
* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.3

* Wed May 29 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package
