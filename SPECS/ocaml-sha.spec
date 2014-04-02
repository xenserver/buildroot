Name:           ocaml-sha
Version:        1.9
Release:        1
Summary:        OCaml SHA
License:        LGPL2.1
Group:          Development/Other
URL:            http://github.com/vincenthz/ocaml-sha
Source0:        https://github.com/xapi-project/ocaml-sha/archive/ocaml-sha-v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
This is a set of C bindings for computing SHA digests.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-v%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc README

%{_libdir}/ocaml/sha/META
%{_libdir}/ocaml/sha/libsha.a
%{_libdir}/ocaml/sha/libsha1.a
%{_libdir}/ocaml/sha/libsha256.a
%{_libdir}/ocaml/sha/libsha512.a
%{_libdir}/ocaml/sha/sha.a
%{_libdir}/ocaml/sha/sha.cma
%{_libdir}/ocaml/sha/sha.cmxa
%{_libdir}/ocaml/sha/sha1.a
%{_libdir}/ocaml/sha/sha1.cma
%{_libdir}/ocaml/sha/sha1.cmi
%{_libdir}/ocaml/sha/sha1.cmx
%{_libdir}/ocaml/sha/sha1.cmxa
%{_libdir}/ocaml/sha/sha256.a
%{_libdir}/ocaml/sha/sha256.cma
%{_libdir}/ocaml/sha/sha256.cmi
%{_libdir}/ocaml/sha/sha256.cmx
%{_libdir}/ocaml/sha/sha256.cmxa
%{_libdir}/ocaml/sha/sha512.a
%{_libdir}/ocaml/sha/sha512.cma
%{_libdir}/ocaml/sha/sha512.cmi
%{_libdir}/ocaml/sha/sha512.cmx
%{_libdir}/ocaml/sha/sha512.cmxa
%{_libdir}/ocaml/sha/dllsha.so
%{_libdir}/ocaml/sha/dllsha1.so
%{_libdir}/ocaml/sha/dllsha256.so
%{_libdir}/ocaml/sha/dllsha512.so

%changelog
* Fri Nov 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package
