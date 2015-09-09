Name:           ocaml-backtrace
Version:        0.3
Release:        1%{?dist}
Summary:        Library for processing backtraces across hosts/processes/languages
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/backtrace
Source0:        https://github.com/xapi-project/backtrace/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpc-devel

%description
A library to help capture and process backtraces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-sexplib-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n backtrace-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install


%files
%doc README.md
%{_libdir}/ocaml/xapi-backtrace
%exclude %{_libdir}/ocaml/xapi-backtrace/*.a
%exclude %{_libdir}/ocaml/xapi-backtrace/*.cmxa
%exclude %{_libdir}/ocaml/xapi-backtrace/*.cmx
%exclude %{_libdir}/ocaml/xapi-backtrace/*.mli


%files devel
%{_libdir}/ocaml/xapi-backtrace/*.a
%{_libdir}/ocaml/xapi-backtrace/*.cmx
%{_libdir}/ocaml/xapi-backtrace/*.cmxa
%{_libdir}/ocaml/xapi-backtrace/*.mli


%changelog
* Wed Sep 9 2015 David Scott <dave.scott@citrix.com> - 0.3-1
- Update to 0.3

* Sun Nov 2 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
