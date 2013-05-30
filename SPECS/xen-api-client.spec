Name:           ocaml-xen-api-client
Version:        0.9.2
Release:        0
Summary:        XenServer XenAPI Client Library for OCaml
License:        LGPLv2
Group:          Development/Libraries
URL:            https://github.com/xen-org/xen-api-client
Source0:        xen-api-client-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-lwt ocaml-ssl ocaml-ounit ocaml-cohttp ocaml-uri ocaml-xmlm ocaml-rpc
Requires:       ocaml ocaml-findlib

%description
XenAPI Client is an OCaml library implementing XenServer's XenAPI.
It is used for programmatically controlling a pool of XenServer
virtualization hosts.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md CHANGES
%{_libdir}/ocaml/xen-api-client/*


%changelog
* Wed May 29 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package
