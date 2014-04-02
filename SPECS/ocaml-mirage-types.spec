%define debug_package %{nil}

Name:           ocaml-mirage-types
Version:        1.1.1
Release:        1
Summary:        MirageOS interfaces
License:        ISC
Group:          Development/Other
URL:            https://github.com/mirage/mirage
Source0:        http://github.com/mirage/mirage/archive/%{version}/mirage-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib-devel ocaml-cstruct-devel ocaml-ounit-devel ocaml-lwt-devel ocaml-ipaddr-devel ocaml-io-page-devel
Requires:       ocaml ocaml-findlib

%description
This library contains interfaces to build applications that are compatible with the Mirage operating system. It defines only interfaces, and no concrete modules.

See http://openmirage.org for more information.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-%{version}

%build
make build-types

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
#export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install-types

%clean
rm -rf %{buildroot}

%files
%{_libdir}/ocaml/mirage-types
%exclude %{_libdir}/ocaml/mirage-types/*.mli

%files devel
%{_libdir}/ocaml/mirage-types/*.mli


%changelog
* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 1.1.1-1
- Initial package
