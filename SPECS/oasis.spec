Name:		oasis
Version:	0.4.4
Release:	1%{?dist}
Summary:	Architecture for building OCaml libraries and applications

Group:          Development/Tools
License:	LGPL
URL:		http://oasis.forge.ocamlcore.org/index.html
Source0:	https://github.com/ocaml/oasis/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocamlify
BuildRequires:	ocamlmod
BuildRequires:	ocaml-ocamldoc
BuildRequires:	ocaml-odn-devel
Requires:	ocaml

%description
OASIS generates a full configure, build and install system for your
application. It starts with a simple `_oasis` file at the toplevel of
your project and creates everything required.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# The auto-requirements script mistakenly thinks that the Oasis library
# modules depend on OASISAstTypes.
%{?filter_setup:
%filter_from_requires /OASISAstTypes/d
%filter_setup
}

%prep
%setup -q


%build
ocaml setup.ml -configure --prefix %{_prefix} --destdir %{buildroot}
ocaml setup.ml -build


%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install



%files
%{_bindir}/oasis

%{_libdir}/ocaml/plugin-loader/META
%{_libdir}/ocaml/plugin-loader/*.cma
%{_libdir}/ocaml/plugin-loader/*.cmi

%{_libdir}/ocaml/oasis/META
%{_libdir}/ocaml/oasis/*.cma
%{_libdir}/ocaml/oasis/*.cmi
%{_libdir}/ocaml/oasis/*.mli

%{_libdir}/ocaml/userconf/META
%{_libdir}/ocaml/userconf/*.cma
%{_libdir}/ocaml/userconf/*.cmi



%files devel
%{_libdir}/ocaml/plugin-loader/*.a
%{_libdir}/ocaml/plugin-loader/*.cmx
%{_libdir}/ocaml/plugin-loader/*.cmxa
%exclude %{_libdir}/ocaml/plugin-loader/*.cmxs
%exclude %{_libdir}/ocaml/plugin-loader/*.ml

%{_libdir}/ocaml/oasis/*.a
%{_libdir}/ocaml/oasis/*.cmx
%{_libdir}/ocaml/oasis/*.cmxa
%exclude %{_libdir}/ocaml/oasis/*.cmxs
%exclude %{_libdir}/ocaml/oasis/*.ml

%{_libdir}/ocaml/userconf/*.a
%{_libdir}/ocaml/userconf/*.cmx
%{_libdir}/ocaml/userconf/*.cmxa
%exclude %{_libdir}/ocaml/userconf/*.cmxs
%exclude %{_libdir}/ocaml/userconf/*.ml


%changelog
* Wed Mar 26 2014 Euan Harris <euan.harris@citrix.com> - 0.4.4-1
- Initial package

