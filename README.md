xen-api-rpm-buildroot
=====================

RPM buildroot for xen-api and related packages. To use this, clone the
repo into ~/rpmbuild. You'll need to set up a user to run mock.

Using mock to build these RPMs:
-------------------------------

```
useradd <user> -G mock
passwd <user>

su - <user>

git clone git://github.com/xen-org/xen-api-rpm-buildroot.git /home/<user>/rpmbuild

./configure.sh
sudo cp xenserver.cfg /etc/mock/

./makemake.py > Makefile
make
```
