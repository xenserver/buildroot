%global debug_package %{nil}

Name:           ocaml-fieldslib
Version:        109.20.00
Release:        1%{?dist}
Summary:        OCaml record fields as first class values

Group:          Development/Libraries
License:        LGPLv2+ with exceptions and BSD
URL:            https://ocaml.janestreet.com
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/fieldslib-%{version}.tar.gz

BuildRequires:  ocaml >= 4.00.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-type-conv

%description
OCaml record fields as first class values

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-camlp4-devel%{?_isa}
Requires:       ocaml-type-conv%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n fieldslib-%{version}

%build
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
#This space intentionally left blank

%files devel
%doc COPYRIGHT.txt INRIA-DISCLAIMER.txt INSTALL.txt LICENSE.txt THIRD-PARTY.txt
%{_libdir}/ocaml/fieldslib

%changelog
* Tue May 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 109.20.00-1
- Initial package

