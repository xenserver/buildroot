xenserver-core
==============

Buildroot for xen-api and related packages, producing RPM and (experimentally) Debian packages.

RPM-based distributions
-----------------------

On RPM-based distributions, the packages are built using `mock`.
To install it on a RHEL/CentOS system then you will need to add the
[EPEL repositories](http://fedoraproject.org/wiki/EPEL). 
Here is a useful article for [CentOS](http://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x).


After adding EPEL, install and set up mock:

```
yum install -y mock redhat-lsb-core
```

Mock will refuse to run as root. You must choose a non-privileged user to
run mock as. Type the following as root:

(Note select a `<user>` which isn't "mock" when typing the commands below)

```
useradd <user> -G mock
passwd <user>

su - <user>
```

You are now ready to clone the xenserver-core repository and build the packages:

```
git clone git://github.com/xenserver/xenserver-core.git
cd xenserver-core

./configure.sh
make
```

Finally, install the packages you have just built, run the install wizard to configure your system to boot Xen and start the xenserver-core components on boot, then reboot:
```
make install
xenserver-install-wizard
reboot
```


Debian-based distributions (experimental)
-----------------------------------------

Building Debian packages is experimental!

On Debian-based distributions, the packages are built using `pbuilder`.
`pbuilder` is available in the main Ubuntu and Debian package repositories, so there is no need to add extra ones.
`pbuilder` does run as root, so you may wish to add your user to the `sudoers` list.

The build also depends on a more modern OCaml compiler than the version in Ubuntu, available from this PPA:
```
deb http://ppa.launchpad.net/louis-gesbert/ocp/ubuntu raring main
deb-src http://ppa.launchpad.net/louis-gesbert/ocp/ubuntu raring main
```

The steps to build Debian packages are the same as those to build RPMs:

```
git clone git://github.com/xenserver/xenserver-core.git
cd xenserver-core

./configure.sh
make

make install
xenserver-install-wizard
reboot
```
