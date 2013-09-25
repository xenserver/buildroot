Name:           libxl-headers
Version:        0.1.0
Release:        1
Summary:        Hack around missing files in Debian's xen-hypervisor package
License:        GPL
Group:          Development/Other
Source0:        libxl_event.h
Source1:        libxl.h
Source2:        libxl_json.h
Source3:        _libxl_list.h
Source4:        _libxl_types.h
Source5:        _libxl_types_json.h
Source6:        libxl_utils.h
Source7:        libxl_uuid.h
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  xen xen-utils ocaml
Requires:       xen xen-utils



%description
Header files not included in Ubuntu's xen-hypervisor package

%prep
%setup -c -T
cp %{SOURCE0} libxl_event.h
cp %{SOURCE1} libxl.h
cp %{SOURCE2} libxl_json.h
cp %{SOURCE3} _libxl_list.h
cp %{SOURCE4} _libxl_types.h
cp %{SOURCE5} _libxl_types_json.h
cp %{SOURCE6} libxl_utils.h
cp %{SOURCE7} libxl_uuid.h

%build

%install
rm -rf %{buildroot}
mkdir %{buildroot}
mkdir -p %{buildroot}/usr/include
install -m 0755 libxl_event.h %{buildroot}/%{_includedir}/libxl_event.h
install -m 0755 libxl.h %{buildroot}/%{_includedir}/libxl.h
install -m 0755 libxl_json.h %{buildroot}/%{_includedir}/libxl_json.h
install -m 0755 _libxl_list.h %{buildroot}/%{_includedir}/_libxl_list.h
install -m 0755 _libxl_types.h %{buildroot}/%{_includedir}/_libxl_types.h
install -m 0755 _libxl_types_json.h %{buildroot}/%{_includedir}/_libxl_types_json.h
install -m 0755 libxl_utils.h %{buildroot}/%{_includedir}/libxl_utils.h
install -m 0755 libxl_uuid.h %{buildroot}/%{_includedir}/libxl_uuid.h

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_includedir}/*

%changelog
* Mon Aug 19 2013 Euan Harris <euan.harris@citrix.com>
- Initial package

