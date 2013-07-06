Name:           xenserver-tech-preview-release
Version:        0.2.0
Release:        0
Summary:        Yum repositories for xenserver
License:        GPL
Group:          Development/Other
URL:            http://www.xen.org/
Source0:        fusion-release-xapi.repo
Source1:        fusion-release-xen-c6.repo
Source2:        fusion-release-xen-c6-RC1.repo
Source3:        fusion-release-epel.repo
Source4:        fusion-release-epel-testing.repo
Source5:        fusion-release-remi.repo
Source6:        fusion-release-RPM-GPG-KEY-EPEL-6
Source7:        fusion-release-RPM-GPG-KEY-remi

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
A virtual package which installs the xenserver yum repos.

%prep

%build

%install
mkdir -p %{buildroot}/etc/yum.repos.d
install -m 0644 %{_sourcedir}/fusion-release-xapi.repo %{buildroot}/etc/yum.repos.d/xapi.repo
#install -m 0644 %{_sourcedir}/fusion-release-xen-c6.repo %{buildroot}/etc/yum.repos.d/xen-c6.repo
#install -m 0644 %{_sourcedir}/fusion-release-xen-c6-RC1.repo %{buildroot}/etc/yum.repos.d/xen-c6-RC1.repo
install -m 0644 %{_sourcedir}/fusion-release-epel.repo %{buildroot}/etc/yum.repos.d/epel.repo
install -m 0644 %{_sourcedir}/fusion-release-epel-testing.repo %{buildroot}/etc/yum.repos.d/epel-testing.repo
install -m 0644 %{_sourcedir}/fusion-release-remi.repo %{buildroot}/etc/yum.repos.d/remi.repo
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
install -m 0644 %{_sourcedir}/fusion-release-RPM-GPG-KEY-EPEL-6 %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
install -m 0644 %{_sourcedir}/fusion-release-RPM-GPG-KEY-remi %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-remi

%clean
rm -rf %{buildroot}

%post
yum repolist

%postun
yum repolist

%files
%defattr(-,root,root)
/etc/yum.repos.d/xapi.repo
#/etc/yum.repos.d/xen-c6.repo
#/etc/yum.repos.d/xen-c6-RC1.repo
/etc/yum.repos.d/epel.repo
/etc/yum.repos.d/epel-testing.repo
/etc/yum.repos.d/remi.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
/etc/pki/rpm-gpg/RPM-GPG-KEY-remi

%changelog
* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

