Name:           ocaml-libvhd
Version:        0.9.0
Release:        0
Summary:        vhd manipulation via libvhd
License:        BSD3
Group:          Development/Other
URL:            http://github.com/xen-org/libvhd
Source0:        https://github.com/xen-org/libvhd/archive/libvhd-0.9.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
Simple C bindings which allow .vhd files to be manipulated.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n libvhd-libvhd-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc ChangeLog README.md
%{_libdir}/ocaml/libvhd/*

%changelog
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

