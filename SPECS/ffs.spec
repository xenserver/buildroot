Name:           ffs
Version:        0.9.3
Release:        0
Summary:        Simple flat file storage manager for the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xen-org/ffs/archive/ffs-%{version}.tar.gz
Source0:        ffs-%{version}.tar.gz
Source1:        ffs-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel cmdliner-devel
BuildRequires:  ocaml-oclock-devel

%description
Simple flat file storage manager for the xapi toolstack.

%prep
%setup -q -n ffs-ffs-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/ffs/ffs %{buildroot}/%{_sbindir}/ffs
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 %{_sourcedir}/ffs-init %{buildroot}%{_sysconfdir}/init.d/ffs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/ffs
%{_sysconfdir}/init.d/ffs

%post
/sbin/chkconfig --add ffs

%preun
if [ $1 -eq 0 ]; then
  /sbin/service ffs stop > /dev/null 2>&1
  /sbin/chkconfig --del ffs
fi

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

