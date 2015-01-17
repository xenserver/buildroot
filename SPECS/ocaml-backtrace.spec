%define planex_version 0.1
%define planex_release 1

Name:           ocaml-backtrace
Version:        %{planex_version}
Release:        %{planex_release}
Summary:        Library for processing backtraces across hosts/processes/languages
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/backtrace
Source0:        https://github.com/xapi-project/backtrace/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-findlib

%description
A library to help capture and process backtraces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-sexplib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n backtrace

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
%exclude %{_libdir}/ocaml/xapi-backtrace/*.ml
%exclude %{_libdir}/ocaml/xapi-backtrace/*.mli


%files devel
%{_libdir}/ocaml/xapi-backtrace/*.a
%{_libdir}/ocaml/xapi-backtrace/*.cmx
%{_libdir}/ocaml/xapi-backtrace/*.cmxa
%{_libdir}/ocaml/xapi-backtrace/*.mli


%changelog
* Sun Nov 2 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
