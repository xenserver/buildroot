Name:           ocaml-qmp
Version:        0.9.0
Release:        0
Summary:        Pure OCaml implementation of the Qemu Message Protocol (QMP)
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/xapi-project/ocaml-qmp
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-obuild ocaml-yojson-devel cmdliner-devel ocaml-ounit-devel
Requires:       ocaml ocaml-findlib

%description
An implementation of the Qemu Message Protocol (QMP) that allows
an application to command, and receive events from, a running qemu
process.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md LICENSE

%{_libdir}/ocaml/qmp/*

%changelog
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

