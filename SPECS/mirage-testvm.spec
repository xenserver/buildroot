%define debug_package %{nil}

Name:           mirage-testvm
Version:        0.2
Release:        1%{?dist}
Summary:        Simple Mirage test VM
License:        ISC
URL:            https://github.com/mirage/xen-testvm
Source0:        https://github.com/mirage/xen-testvm/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mirage-block-xen-devel
BuildRequires:  ocaml-mirage-console-xen-devel
BuildRequires:  ocaml-mirage-types-devel
BuildRequires:  ocaml-testvmlib-devel
BuildRequires:  ocaml-vchan-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-xen-devel
BuildRequires:  ocaml-mirage-clock-xen-devel
BuildRequires:  ocaml-shared-memory-ring-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-ipaddr-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-gnt-devel
BuildRequires:  ocaml-evtchn-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xenstore-clients-devel

%description
This is a simple Mirage test VM.

%prep
%setup -q -n xen-testvm-%{version}

%build
./manual-build.sh

%install
mkdir -p %{buildroot}/boot/guest
cp mir-test.xen %{buildroot}/boot/guest/mirage-testvm.xen

%files
%doc CHANGES
%doc README.md
/boot/guest/mirage-testvm.xen

%changelog
* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 0.2-1
- Update to 0.2

* Wed Jul 16 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
