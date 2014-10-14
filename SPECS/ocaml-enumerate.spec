%global debug_package %{nil}

Name:           ocaml-enumerate
Version:        111.08.00
Release:        1%{?dist}
Summary:        Quotation expanders for enumerating finite types.

Group:          Development/Libraries
License:        Apache-2.0
URL:            https://ocaml.janestreet.com
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/enumerate-%{version}.tar.gz

BuildRequires:  ocaml >= 4.00.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-type-conv

%description
Quotation expanders for enumerating finite types.

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
%setup -q -n enumerate-%{version}
ocaml setup.ml -configure --prefix %{_prefix} --destdir %{buildroot}

%build
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc README.md
%doc LICENSE.txt
%doc THIRD-PARTY.txt
%doc INRIA-DISCLAIMER.txt
%doc INSTALL.txt
%{_libdir}/ocaml/enumerate
%exclude %{_libdir}/ocaml/enumerate/*.a
%exclude %{_libdir}/ocaml/enumerate/*.cmxa
%exclude %{_libdir}/ocaml/enumerate/*.cmx
%exclude %{_libdir}/ocaml/enumerate/*.mli

%files devel
%{_libdir}/ocaml/enumerate/*.a
%{_libdir}/ocaml/enumerate/*.cmxa
%{_libdir}/ocaml/enumerate/*.cmx
%{_libdir}/ocaml/enumerate/*.mli

%changelog
* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 111.03.00-1
- Initial package

