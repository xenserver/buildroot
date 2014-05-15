Name:           xen-missing-headers
Version:        4.4
Release:        1%{?dist}
Summary:        Headers missing from the ARM xen-4.4 package
License:        GPL
Group:          Development/Libraries
URL:            http://xenproject.org/
Source0:        xen-missing-headers_usr_include_xen_arch-arm_hvm_save.h

%description
Headers missing from the ARM xen-4.4 package.

%prep

%build

%install
mkdir %{_buildroot}/usr/include/xen/arch-arm/hvm
cp xen-missing-headers_usr_include_xen_arch-arm_hvm_save.h %{_buildroot}/usr/include/xen/arch-arm/hvm/save.h

%files
/usr/include/xen/arch-arm/hvm/save.h

%changelog
* Thu May 15 2014 David Scott <dave.scott@eu.citrix.com> - 4.4-1
- Initial package

