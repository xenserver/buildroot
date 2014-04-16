Name:           ocaml-uutf
Version:        0.9.3
Release:        2%{?dist}
Summary:        Non-blocking streaming codec for UTF-8, UTF-16, UTF-16LE and UTF-16BE
License:        BSD3
Group:          Development/Libraries
URL:            http://erratique.ch/software/uutf
Source0:        http://erratique.ch/software/uutf/releases/uutf-%{version}.tbz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
Requires:       ocaml

%description
Uutf is an non-blocking streaming Unicode codec for OCaml to decode and
encode the UTF-8, UTF-16, UTF-16LE and UTF-16BE encoding schemes. It can
efficiently work character by character without blocking on IO. Decoders
perform character position tracking and support newline normalization.

Functions are also provided to fold over the characters of UTF encoded
OCaml string values and to directly encode characters in OCaml Buffer.t
values.

Uutf is made of a single, independent, module and distributed under the
BSD3 license.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uutf-%{version}

%build
./pkg/pkg-git
./pkg/build true

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}%{_libdir}/ocaml/uutf
(cd _build/src; ocamlfind install uutf ../pkg/META uutf.mli uutf.cmi uutf.cmx uutf.cma uutf.a uutf.cma uutf.cmxa uutf.cmxs)
#ocamlfind install uutf _build/pkg/META _build/src/uutf.{mli,cmi,cmx,cma,a,cmxa,cmxs}


%files
%{_libdir}/ocaml/uutf/META
%{_libdir}/ocaml/uutf/uutf.cmi
%{_libdir}/ocaml/uutf/uutf.cma

%files devel
%{_libdir}/ocaml/uutf/uutf.cmx
%{_libdir}/ocaml/uutf/uutf.cmxa
%{_libdir}/ocaml/uutf/uutf.cmxs
%{_libdir}/ocaml/uutf/uutf.a
%{_libdir}/ocaml/uutf/uutf.mli


%changelog
* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-2
- 'Ported' from xen-dist-ocaml to xenserver-core

* Fri Oct 11 2013 Jon Ludlam <jonathan.ludlam@eu.citrix.com> - 0.9.3-1
- Initial RPM release 
