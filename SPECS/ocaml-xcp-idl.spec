%global debug_package %{nil}

Name:           ocaml-xcp-idl
Version:        0.9.14
Release:        1
Summary:        Common interface definitions for XCP services
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/xcp-idl
Source0:        https://github.com/djs55/xcp-idl/archive/%{version}/xcp-idl-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-cohttp-devel xmlm-devel ocaml-rpc-devel message-switch-devel cmdliner-devel ocaml-fd-send-recv-devel ocaml-xcp-rrd-devel
BuildRequires:  ocaml-ounit-devel

# XXX transitive dependencies of message-switch-devel
BuildRequires: ocaml-oclock-devel

#  "uri"
#"re"
#           "cohttp"
#           "xmlm"
#           "rpc" {> "1.4.0"}
#           "ocamlfind"
#           "syslog"
#           "message_switch"
Requires:       ocaml ocaml-findlib

%description
Common interface definitions for XCP services.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}
Requires:       message-switch-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-idl-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xcp/*

%changelog
* Thu Sep 26 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.14-1
- Support searching for executables on the XCP_PATH as well as the PATH

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Logging, channel passing and interface updates

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.12-1
- Allow domain 0 memory policy to be queried

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

