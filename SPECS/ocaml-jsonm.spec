Name:           ocaml-jsonm
Version:        0.9.1
Release:        1%{?dist}
Summary:        Non-blocking streaming JSON codec for OCaml
License:        BSD3
URL:            http://erratique.ch/software/jsonm
Source0:        https://github.com/dbuenzli/jsonm/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-uutf-devel
BuildRequires:  oasis

%description
Jsonm is a non-blocking streaming codec to decode and encode the JSON
data format. It can process JSON text without blocking on IO and
without a complete in-memory representation of the data.

The alternative "uncut" codec also processes whitespace and
(non-standard) JSON with JavaScript comments.

Jsonm is made of a single module and depends on [Uutf][1]. It is
distributed under the BSD3 license.

[1]: http://erratique.ch/software/uutf

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-uutf-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n jsonm-%{version}

%build
rm _tags
oasis setup
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir} \
      --destdir $RPM_BUILD_ROOT
ocaml setup.ml -build 

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p %{buildroot}/%{_bindir}
ocaml setup.ml -install

%files
%doc CHANGES
%doc README
%{_libdir}/ocaml/jsonm
%exclude %{_libdir}/ocaml/jsonm/*.a
%exclude %{_libdir}/ocaml/jsonm/*.cmxa
%exclude %{_libdir}/ocaml/jsonm/*.cmx
%exclude %{_libdir}/ocaml/jsonm/*.mli
%{_bindir}/jsontrip
%{_bindir}/ocamltweets

%files devel
%{_libdir}/ocaml/jsonm/*.a
%{_libdir}/ocaml/jsonm/*.cmxa
%{_libdir}/ocaml/jsonm/*.cmx
%{_libdir}/ocaml/jsonm/*.mli

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citri.com> - 0.9.1-1
- Initial package
