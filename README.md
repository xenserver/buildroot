xen-api-rpm-buildroot
=====================

RPM buildroot for xen-api and related packages. To use this, clone the
repo into ~/rpmbuild. You'll need to set up a user to run mock.

Installing mock
---------------

First if running a RHEL/CentOS system then you will need to add the
[EPEL repositories](http://fedoraproject.org/wiki/EPEL). Here is a useful
article for [CentOS](http://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x).
After installing mock, type:

```
yum install -y mock
```

Using mock to build these RPMs:
-------------------------------

Mock will refuse to run as root. You must choose a non-privileged user to
run mock as. Type the following as root:

(Note select a "<user>" which isn't "mock" when typing the commands below)

```
useradd <user> -G mock
passwd <user>

su - <user>

git clone git://github.com/xen-org/xen-api-rpm-buildroot.git rpmbuild

cd rpmbuild

./configure.sh

./makemake.py > Makefile

make
```
