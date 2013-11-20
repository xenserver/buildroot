Name:           xenserver-core-latest-snapshot
Version:        0.1.0
Release:        2
Summary:        Yum repositories for xenserver
License:        GPL
Group:          Development/Other
URL:            http://www.xenserver.org/
Source0:        fusion-release-xapi.repo
Source1:        fusion-release-xen-c6.repo
Source2:        fusion-release-xen-c6-RC1.repo
Source3:        fusion-release-epel.repo
Source4:        fusion-release-epel-testing.repo
Source5:        fusion-release-remi.repo
Source6:        fusion-release-RPM-GPG-KEY-EPEL-6
Source7:        fusion-release-RPM-GPG-KEY-remi
Source8:        fusion-release-xen-c6-tweaked.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
A virtual package which installs the xenserver yum repos.

%prep
%setup -c -T
cp %{SOURCE0} fusion-release-xapi.repo
cp %{SOURCE1} fusion-release-xen-c6.repo
cp %{SOURCE2} fusion-release-xen-c6-RC1.repo
cp %{SOURCE3} fusion-release-epel.repo
cp %{SOURCE4} fusion-release-epel-testing.repo
cp %{SOURCE5} fusion-release-remi.repo
cp %{SOURCE6} fusion-release-RPM-GPG-KEY-EPEL-6
cp %{SOURCE7} fusion-release-RPM-GPG-KEY-remi
cp %{SOURCE8} fusion-release-xen-c6-tweaked.repo

%build

%install
mkdir -p %{buildroot}/etc/yum.repos.d
install -m 0644 fusion-release-xapi.repo %{buildroot}/etc/yum.repos.d/xapi.repo
install -m 0644 fusion-release-xen-c6-tweaked.repo %{buildroot}/etc/yum.repos.d/xen-c6-tweaked.repo
#install -m 0644 fusion-release-xen-c6.repo %{buildroot}/etc/yum.repos.d/xen-c6.repo
#install -m 0644 fusion-release-xen-c6-RC1.repo %{buildroot}/etc/yum.repos.d/xen-c6-RC1.repo
install -m 0644 fusion-release-epel.repo %{buildroot}/etc/yum.repos.d/epel.repo
install -m 0644 fusion-release-epel-testing.repo %{buildroot}/etc/yum.repos.d/epel-testing.repo
install -m 0644 fusion-release-remi.repo %{buildroot}/etc/yum.repos.d/remi.repo
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
install -m 0644 fusion-release-RPM-GPG-KEY-EPEL-6 %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
install -m 0644 fusion-release-RPM-GPG-KEY-remi %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-remi

%clean
rm -rf %{buildroot}

%post
yum repolist

%postun
yum repolist

%files
%defattr(-,root,root)
/etc/yum.repos.d/xapi.repo
/etc/yum.repos.d/xen-c6-tweaked.repo
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

