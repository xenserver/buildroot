Name:           ocaml-opasswd
Version:        0.9.0
Release:        0
Summary:        OCaml interface to the glibc passwd/shadow password functions
License:        ISC
Group:          Development/Other
URL:            http://github.com/xapi-project/ocaml-opasswd
Source0:        https://github.com/xapi-project/ocaml-opasswd/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         ocaml-opasswd-ocaml-4.00.1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ctypes-devel
Requires:       ocaml ocaml-findlib

%description
This is an OCaml binding to the glibc passwd file and shadow password
file interface. It can be used to read, parse, manipulate and write
passwd and shadow files on Linux systems. It might also work on other
nixes, but it has not been tested.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
ocaml setup.ml -install
rm -f %{buildroot}%{_libdir}/ocaml/usr/local/bin/opasswd_test

%clean
rm -rf %{buildroot}

%files
%doc README.md
%{_libdir}/ocaml/oPasswd
%exclude %{_libdir}/ocaml/oPasswd/*.a
%exclude %{_libdir}/ocaml/oPasswd/*.cmxa
%exclude %{_libdir}/ocaml/oPasswd/*.mli

%files devel
%{_libdir}/ocaml/oPasswd/*.a
%{_libdir}/ocaml/oPasswd/*.cmxa
%{_libdir}/ocaml/oPasswd/*.mli

%changelog
* Thu Apr 24 2014 David Scott <dave.scott@citrix.com>
- Fix split between -devel and main package, hopefully

* Thu Oct 31 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package

