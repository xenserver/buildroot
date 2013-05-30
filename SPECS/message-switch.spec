Name:           message-switch
Version:        0.9.0
Release:        0
Summary:        A store and forward message switch
License:        FreeBSD
Group:          Development/Other
URL:            https://github.com/xen-org/message-switch/archive/message-switch-0.9.0.tar.gz
Source0:        message-switch-0.9.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib
#  "ocamlfind"
#  "cohttp" {= "0.9.7"}
#  "rpc"
#  "xenstore"
#  "ounit"
#  "syslog"
#  "uri"
#  "re"
#  "rpc"
#  "cmdliner"
#  "ssl"
#  "oclock"

%description
A store and forward message switch for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n message-switch-message-switch-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog
%{_libdir}/ocaml/message_switch/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

