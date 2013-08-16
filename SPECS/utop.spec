Name:           utop
Version:        1.5
Release:        1
Summary:        utop is a toplevel for OCaml which can run in a terminal or in emacs. It supports completion, colors, parenthesis matching, ...
License:        BSD
Group:          Development/Other
URL:            https://github.com/diml/utop/archives/%{version}.tar.gz
Source0:        https://github.com/diml/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc
BuildRequires:  ocaml-zed-devel ocaml-lambda-term-devel
Requires: ocaml-camomile-data

%description
utop is a toplevel for OCaml which can run in a terminal or in emacs. It supports completion, colors, parenthesis matching, ...

%prep
%setup -q

%build
ocaml setup.ml -configure --prefix %{_prefix} --destdir %{buildroot}
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE CHANGES.md
%{_bindir}/utop
%{_bindir}/utop-full
%{_libdir}/ocaml/utop/*
/usr/share/emacs/site-lisp/utop.el

%changelog
* Fri Jun 21 2013 David Scott <dave.scott@eu.citrix.com>
- Update to version 1.5 (discovered lurking in plain sight on github)

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

