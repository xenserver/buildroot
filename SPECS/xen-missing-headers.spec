Name:           xen-missing-headers
Version:        4.4
Release:        4%{?dist}
Summary:        Headers missing from the ARM xen-4.4 package
License:        GPL
Group:          Development/Libraries
URL:            http://xenproject.org/
Source0:        xen-missing-headers_usr_include_xen_arch-arm_hvm_save.h 

%description
Headers missing from the ARM xen-4.4 package.

%prep
cp %{SOURCE0} save.h

%build
touch save.h

%install
mkdir -p %{buildroot}/usr/include/xen/arch-arm/hvm
cp save.h %{buildroot}/usr/include/xen/arch-arm/hvm/save.h

%files
/usr/include/xen/arch-arm/hvm/save.h

%changelog
* Tue Aug 18 2014 Bob Ball <bob.ball@citrix.com> - 4.4-4
- Fix spec file typo

* Thu May 15 2014 David Scott <dave.scott@eu.citrix.com> - 4.4-3
- Initial package

