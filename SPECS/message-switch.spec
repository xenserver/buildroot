Name:           message-switch
Version:        0.10.1
Release:        1
Summary:        A store and forward message switch
License:        FreeBSD
Group:          Development/Other
URL:            https://github.com/xapi-project/message-switch/archive/message-switch-%{version}.tar.gz
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        message-switch-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
BuildRequires: ocaml-cohttp-devel ocaml-rpc-devel ocaml-xenstore-devel
BuildRequires: ocaml-ounit-devel ocaml-uri-devel
BuildRequires: ocaml-re-devel ocaml-rpc-devel cmdliner-devel
BuildRequires: ocaml-ssl-devel ocaml-oclock-devel
BuildRequires: openssl openssl-devel
Requires:      redhat-lsb-core
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

%prep
%setup -q
cp %{SOURCE1} message-switch-init

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install switch_main.native %{buildroot}/%{_sbindir}/message-switch
install main.native %{buildroot}/%{_sbindir}/message-cli
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 message-switch-init %{buildroot}%{_sysconfdir}/init.d/message-switch

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/message-switch
%{_sbindir}/message-cli
%{_sysconfdir}/init.d/message-switch

%post
/sbin/chkconfig --add message-switch

%preun
if [ $1 -eq 0 ]; then
  /sbin/service message-switch stop > /dev/null 2>&1
  /sbin/chkconfig --del message-switch
fi

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}
Requires:       ocaml ocaml-findlib

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog
%{_libdir}/ocaml/message_switch/*

%changelog
* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.10.1 which is more tolerant of startup orderings

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

