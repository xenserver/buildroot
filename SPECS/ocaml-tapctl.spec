%global debug_package %{nil}

Name:           ocaml-tapctl
Version:        0.9.1
Release:        2%{?dist}
Summary:        Manipulate running tapdisk instances
License:        LGPL
URL:            https://github.com/xapi-project/tapctl
Source0:        https://github.com/xapi-project/tapctl/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel

%description
Manipulate running tapdisk instances on a xen host.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n tapctl-%{version}

%build
./configure --destdir %{buildroot}/%{_libdir}/ocaml
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export OCAMLFIND_LDCONF=ignore
make install

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{_libdir}/ocaml/tapctl
%exclude %{_libdir}/ocaml/tapctl/*.a
%exclude %{_libdir}/ocaml/tapctl/*.cmxa
%exclude %{_libdir}/ocaml/tapctl/*.cmx
%exclude %{_libdir}/ocaml/tapctl/*.mli

%files devel
%{_libdir}/ocaml/tapctl/*.a
%{_libdir}/ocaml/tapctl/*.cmx
%{_libdir}/ocaml/tapctl/*.cmxa
%{_libdir}/ocaml/tapctl/*.mli

%changelog
* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.1-2
- Split files correctly between base and devel packages

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

