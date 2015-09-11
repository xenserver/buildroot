Name:           xapi-storage-datapath-plugins
Version:        0.1
Release:        1%{?dist}
Summary:        Storage datapath plugins for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xapi-storage-datapath-plugins
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       xapi-storage

%description
Storage datapath plugins for the xapi toolstack.

%prep
%setup -q

%build

%install
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script/ PYTHONDIR=/usr/lib/python2.7/site-packages/xapi/storage/datapath make install
(cd %{buildroot}/%{_libexecdir}/xapi-storage-script/datapath; rm -f raw+file; ln -s loop+blkback raw+file)

%files
%doc README.md LICENSE
%{_libexecdir}/xapi-storage-script/datapath/raw+file
%{_libexecdir}/xapi-storage-script/datapath/vhd+file
%{_libexecdir}/xapi-storage-script/datapath/loop+blkback/*
%{_libexecdir}/xapi-storage-script/datapath/tapdisk/*
/usr/lib/python2.7/site-packages/xapi/storage/datapath/*.py*

%changelog
* Fri Sep 11 2015 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package

