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
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

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
%setup -q -n message-switch-message-switch-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install switch.native %{buildroot}/%{_sbindir}/message-switch
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/message-switch-init %{buildroot}%{_sysconfdir}/init.d/message-switch

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/message-switch
%{_sysconfdir}/init.d/message-switch

%post
/sbin/chkconfig --add message-switch

%preun
if [$1 -eq 0 ]; then
  /sbin/service message-switch stop > /dev/null 2>&1
  /sbin/chkconfig --del message-switch
fi

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog
%{_libdir}/ocaml/message_switch/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

