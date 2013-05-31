Name:           deriving-ocsigen
Version:        0.3c
Release:        0
Summary:        Extension to OCaml for deriving functions from type declarations
License:        MIT
Group:          Development/Other
URL:            http://ocsigen.org/download/deriving-ocsigen-0.3c.tar.gz
Source0:        deriving-ocsigen-0.3c.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
# re uri cstruct lwt ounit
Requires:       ocaml ocaml-findlib

%description
Extension to OCaml for deriving functions from type declarations

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n deriving-ocsigen-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc COPYING README CHANGES
%{_libdir}/ocaml/deriving-ocsigen/*

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

