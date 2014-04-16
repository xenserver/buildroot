%global debug_package %{nil}

Name:           ocaml-fd-send-recv
Version:        1.0.1
Release:        1%{?dist}
Summary:        Bindings to sendmsg/recvmsg for fd passing under Linux
License:        LGPL
Group:          Development/Libraries
URL:            http://github.com/xapi-project/ocaml-fd-send-recv
Source0:        https://github.com/xapi-project/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
Requires:       ocaml
Requires:       ocaml-findlib

%description
Bindings to sendmsg/recvmsg for fd passing under Linux.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%doc README.md LICENSE
%{_libdir}/ocaml/fd-send-recv/*
%{_libdir}/ocaml/stublibs/dllfd_send_recv_stubs.so
%{_libdir}/ocaml/stublibs/dllfd_send_recv_stubs.so.owner

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 1.0.1-1
- Initial package

