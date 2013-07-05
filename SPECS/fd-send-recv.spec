Name:           ocaml-fd-send-recv
Version:        1.0.1
Release:        1
Summary:        Bindings to sendmsg/recvmsg for fd passing under Linux
License:        LGPL
Group:          Development/Other
URL:            http://github.com/xen-org/ocaml-fd-send-recv/archive/ocaml-fd-send-recv-1.0.1.tar.gz
Source0:        https://github.com/xen-org/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Bindings to sendmsg/recvmsg for fd passing under Linux.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-fd-send-recv-ocaml-fd-send-recv-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md LICENSE
%{_libdir}/ocaml/fd-send-recv/*
%{_libdir}/ocaml/stublibs/dllfd_send_recv_stubs.so
%{_libdir}/ocaml/stublibs/dllfd_send_recv_stubs.so.owner

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

