Name:           xenvm
Version:        0.1.0
Release:        1%{?dist}
Summary:        A compatible replace for LVM supporting thinly provisioned volumes
License:        LGPL
URL:            https://github.com/xapi-project/xenvm
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-block-unix-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-camldm-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-mirage-clock-unix-devel
BuildRequires:  ocaml-mirage-block-volume-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-shared-block-ring-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  device-mapper-devel
BuildRequires:  libffi-devel
BuildRequires:  oasis

%description
A compatible replacement for LVM supporting thinly provisioned volumes

%prep
%setup -q -n xenvm-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install xenvmd.native %{buildroot}/%{_sbindir}/xenvmd


%files
%doc README.md
%{_sbindir}/xenvmd

%changelog
* Mon Apr 20 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-1
- Initial package

