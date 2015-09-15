# -*- rpm-spec -*-

Summary: Simple LVM storage adapter for xapi
Name:    ezlvm
Version: 0.5.1
Release: 3%{?dist}
License: LGPL
URL:     https://github.com/xapi-project/ezlvm
Source0: https://github.com/xapi-project/ezlvm/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-findlib-devel
BuildRequires: xapi-storage-devel
BuildRequires: xapi-storage
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-uri-devel
BuildRequires: ocamlscript
BuildRequires: ocaml-ounit-devel
Requires: ocaml
Requires: ocaml-camlp4-devel
Requires: ocaml-findlib
Requires: ocaml-findlib-devel
Requires: xapi-storage-devel
Requires: xapi-storage
Requires: ocaml-re-devel
Requires: ocaml-cmdliner-devel
Requires: ocaml-uri-devel
Requires: ocamlscript
Requires: ocaml-ounit-devel
Requires: xapi-storage-datapath-plugins

%description
Simple LVM storage adapter for xapi

%prep 
%setup -q -n %{name}-%{version}

%build
cd src
for i in SR* Volume* Plugin*; do ./$i --help > /dev/null; done

%install
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script make install
echo Now installing compiled files
cd src
for i in *.exe; do
  echo Installing $i
  install -m 0755 $i %{buildroot}%{_libexecdir}/xapi-storage-script/volume/org.xen.xapi.storage.ezlvm/$i
done

%files
%{_libexecdir}/xapi-storage-script/volume/org.xen.xapi.storage.ezlvm/*

%changelog
* Tue Sep 15 2015 David Scott <dave.scott@citrix.com> - 0.5.1-3
- Update to 0.5.1
- Add dependency on xapi-storage-datapath-plugins

* Fri Feb  6 2015 David Scott <dave.scott@citrix.com> - 0.4-1
- Update to 0.4

* Tue Dec 23 2014 David Scott <dave.scott@citrix.com> - 0.3-1
- Update to 0.3

* Sat Nov  1 2014 David Scott <dave.scott@citrix.com> - 0.2.1-1
- Update to 0.2.1

* Fri Oct 17 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
