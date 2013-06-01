Name:           ocaml-syslog
Version:        1.4
Release:        0
Summary:        Syslog bindings for OCaml
License:        LGPL
Group:          Development/Other
URL:            http://opam.ocamlpro.com/pkg/syslog.1.4.html
Source0:        syslog-1.4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Syslog bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n syslog-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc Changelog
%{_libdir}/ocaml/syslog/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

