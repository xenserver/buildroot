Name:           ocaml-omd
Version:        1.0.2
Release:        1%{?dist}
Summary:        A Markdown frontend in pure OCaml.
License:        ISC
URL:            https://github.com/ocaml/omd
Source0:        https://github.com/ocaml/omd/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         ocaml-omd-setup.ml.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
This Markdown library is implemented using only pure OCaml (including
I/O operations provided by the standard OCaml compiler distribution).
OMD is meant to be as faithful as possible to the original Markdown.
Additionally, OMD implements a few Github markdown features, an
extension mechanism, and a few other features. Note that the opam
package installs both the OMD library and the command line tool `omd`.
Note that The library interface of 1.0.x is only partially compatible
with 0.9.x.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n omd-%{version}
%patch0 -p1

%build
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
make install

%files
%{_libdir}/ocaml/omd
%exclude %{_libdir}/ocaml/omd/*.a
%exclude %{_libdir}/ocaml/omd/*.cmxa
%exclude %{_libdir}/ocaml/omd/*.cmx
%exclude %{_libdir}/ocaml/omd/*.mli
%{_bindir}/omd
%{_bindir}/test_cow
%{_bindir}/test_spec

%files devel
%{_libdir}/ocaml/omd/*.a
%{_libdir}/ocaml/omd/*.cmxa
%{_libdir}/ocaml/omd/*.cmx
%{_libdir}/ocaml/omd/*.mli

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 1.0.2-1
- Initial package
