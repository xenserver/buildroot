Name:           utop
Version:        1.5
Release:        1%{?dist}
Summary:        A toplevel for OCaml which can run in a terminal or in Emacs
License:        BSD
Group:          Development/Other
URL:            https://github.com/diml/utop
Source0:        https://github.com/diml/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc
BuildRequires:  ocaml-zed-devel ocaml-lambda-term-devel
Requires: ocaml-camomile-data

%description
utop is a toplevel for OCaml which can run in a terminal or in Emacs. It
supports completion, colors, parenthesis matching, ...

%prep
%setup -q

%build
ocaml setup.ml -configure --prefix %{_prefix} --destdir %{buildroot}
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
%doc README.md LICENSE CHANGES.md
%{_bindir}/utop
%{_bindir}/utop-full
%{_libdir}/ocaml/utop/*
/usr/share/emacs/site-lisp/utop.el

%changelog
* Fri Jun 21 2013 David Scott <dave.scott@eu.citrix.com> - 1.5-1
- Update to version 1.5 (discovered lurking in plain sight on github)

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

