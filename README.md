xen-api-rpm-buildroot
=====================

RPM buildroot for xen-api and related packages. To use this, clone the
repo into ~/rpmbuild. You'll need to set up a user to run mock.

Using mock to build these RPMs:
-------------------------------

```
useradd <user> -G mock
passwd <user>

git clone git://github.com/xen-org/xen-api-rpm-buildroot.git /home/<user>/rpmbuild
mkdir -p /home/<user>/rpmbuild/RPMS/x86_64/
createrepo /home/<user>/rpmbuild/RPMS/x86_64

cp xenserver.cfg /etc/mock/ # edit so last repo points to file:///home/<user>/blah

su - <user>

./makemake.py > Makefile
make
```
