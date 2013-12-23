Name:           forkexecd
Version:        0.9.1
Release:        1
Summary:        A subprocess management service
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/forkexecd
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        forkexecd-init
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-rpc-devel ocaml-fd-send-recv-devel ocaml-re-devel ocaml-uuidm-devel ocaml-stdext-devel ocaml-xcp-idl-devel ocaml-oclock-devel
Requires:  ocaml-rpc ocaml-rpc-devel redhat-lsb-core
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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install fe_main.native %{buildroot}/%{_sbindir}/forkexecd
install fe_cli.native %{buildroot}/%{_sbindir}/forkexecd-cli
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 forkexecd-init %{buildroot}%{_sysconfdir}/init.d/forkexecd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml ocaml-findlib

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%defattr(-,root,root)
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/forkexec/*

%changelog
* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

