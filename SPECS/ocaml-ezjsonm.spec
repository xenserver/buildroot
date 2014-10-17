Name:           ocaml-ezjsonm
Version:        0.2.0
Release:        1%{?dist}
Summary:        An easy interface on top of the Jsonm library
License:        ISC
URL:            https://github.com/samoht/ezjsonm
Source0:        https://github.com/samoht/ezjsonm/archive/0.2.0/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-jsonm-devel

%description
This version provides more convenient (but far less flexible)
input and output functions that go to and from [string] values.
This avoids the need to write signal code, which is useful for
quick scripts that manipulate JSON.

More advanced users should go straight to the Jsonm library and
use it directly, rather than be saddled with the Ezjsonm interface.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-jsonm-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ezjsonm-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%{_libdir}/ocaml/ezjsonm
%exclude %{_libdir}/ocaml/ezjsonm/*.a
%exclude %{_libdir}/ocaml/ezjsonm/*.cmxa
%exclude %{_libdir}/ocaml/ezjsonm/*.cmx
%exclude %{_libdir}/ocaml/ezjsonm/*.mli

%files devel
%{_libdir}/ocaml/ezjsonm/*.a
%{_libdir}/ocaml/ezjsonm/*.cmxa
%{_libdir}/ocaml/ezjsonm/*.cmx
%{_libdir}/ocaml/ezjsonm/*.mli

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.2.0-1
- Initial package
