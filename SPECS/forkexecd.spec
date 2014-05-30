Name:           forkexecd
Version:        0.9.1
Release:        1%{?dist}
Summary:        A subprocess management service
License:        LGPL
URL:            https://github.com/xapi-project/forkexecd
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        forkexecd-init
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel
Requires:  redhat-lsb-core
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

%description
A service which starts and manages subprocesses, avoiding the need to manually
fork() and exec() in a multithreaded program.

%prep
%setup -q
cp %{SOURCE1} forkexecd-init

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install fe_main.native %{buildroot}/%{_sbindir}/forkexecd
install fe_cli.native %{buildroot}/%{_sbindir}/forkexecd-cli
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 forkexecd-init %{buildroot}%{_sysconfdir}/init.d/forkexecd


%files
%{_sbindir}/forkexecd
%{_sbindir}/forkexecd-cli
%{_sysconfdir}/init.d/forkexecd

%post
/sbin/chkconfig --add forkexecd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service forkexecd stop > /dev/null 2>&1
  /sbin/chkconfig --del forkexecd
fi

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-fd-send-recv-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}
Requires:       ocaml-uuidm-devel%{?_isa}
Requires:       ocaml-xcp-idl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/forkexec/*

%changelog
* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

