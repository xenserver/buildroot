Name:           ocaml-lambda-term
Version:        1.2
Release:        1
Summary:        Lambda-Term is a cross-platform library for manipulating the terminal for Ocaml
License:        BSD3
Group:          Development/Other
URL:            http://forge.ocamlcore.org/frs/download.php/945/lambda-term-1.2.tar.gz
Source0:        http://forge.ocamlcore.org/frs/download.php/945/lambda-term-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc ocaml-zed-devel ocaml-lwt-devel ocaml-camomile-devel ocaml-react-devel
Requires:       ocaml ocaml-findlib

%description
Lambda-Term is a cross-platform library for manipulating the terminal.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n lambda-term-%{version}

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

rm -f %{buildroot}/%{_libdir}/ocaml/usr/local/bin/lambda-term-actions
%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc LICENSE CHANGES
%{_libdir}/ocaml/lambda-term/*
%{_libdir}/ocaml/stublibs/dlllambda-term_stubs.so
%{_libdir}/ocaml/stublibs/dlllambda-term_stubs.so.owner

%changelog
* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

