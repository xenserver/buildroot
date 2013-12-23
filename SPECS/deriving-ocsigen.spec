Name:           deriving-ocsigen
Version:        0.3c
Release:        1
Summary:        Extension to OCaml for deriving functions from type declarations
License:        MIT
Group:          Development/Libraries
URL:            http://ocsigen.org/download/deriving-ocsigen-0.3c.tar.gz
Source0:        http://ocsigen.org/download/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib

%description
Extension to OCaml for deriving functions from type declarations

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install


%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc COPYING README CHANGES
%{_libdir}/ocaml/deriving-ocsigen/*

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.3c-1
- Initial package

