Name:           ocaml-dyntype
Version:        0.9.0
Release:        1%{?dist}
Summary:        syntax extension which makes OCaml types and values easier to manipulate programmatically
License:        ISC
URL:            https://github.com/mirage/dyntype/
Source0:        https://github.com/mirage/dyntype/archive/dyntype-0.9.0.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-type-conv
BuildRequires:  ocaml-camlp4-devel

%description
syntax extension which makes OCaml types and values easier to manipulate programmatically

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n dyntype-dyntype-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%{_libdir}/ocaml/dyntype
%exclude %{_libdir}/ocaml/dyntype/*.a
%exclude %{_libdir}/ocaml/dyntype/*.cmxa

%files devel
%{_libdir}/ocaml/dyntype/*.a
%{_libdir}/ocaml/dyntype/*.cmxa

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.9.0-1
- Initial package
