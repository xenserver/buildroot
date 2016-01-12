buildroot
=========

Buildroot for xen-api and related packages, producing RPM and (experimentally) Debian packages.

RPM-based distributions
-----------------------

On RPM-based distributions, the packages are built using `mock`.
To install it on a 64-bit RHEL/CentOS system then you will need to add the
[EPEL repositories](http://fedoraproject.org/wiki/EPEL).   The `epel-release`
package configures yum to use the EPEL repository.   On CentOS, the package
is provided by the CentOS Extras repository, which is enabled by default;
on RHEL, you must enable the 'optional' and 'extras' repositories.   To
enable EPEL, type the following as root:

```
yum install -y epel-release
```

After adding EPEL, install a couple of prerequisites:

```
yum install -y mock redhat-lsb-core centos-release-xen
```

Mock will refuse to run as root. You must choose a non-privileged user to
run mock as. Type the following as root:

(Note select a `<user>` which isn't "mock" when typing the commands below)

```
useradd <user> -G mock
passwd <user>

su - <user>
```

You are now ready to clone the buildroot repository and build the packages:

```
git clone git://github.com/xenserver/buildroot.git
cd buildroot

./configure
make
```

Finally, install the packages you have just built, run the install wizard to configure your system to boot Xen and start the buildroot components on boot, then reboot:
```
make install
xenserver-install-wizard
reboot
```


Debian-based distributions (experimental)
-----------------------------------------

Building Debian packages is experimental!

The Debian/Ubuntu package build uses [cowbuilder](https://wiki.debian.org/cowbuilder), which needs to run as root, so you may wish to add your user to the `sudoers` list.

The build also depends on OCaml 4.01.0, now available in Ubuntu Trusty and Debian Jessie.

The steps to build Debian packages are the same as those to build RPMs:

```
git clone git://github.com/xenserver/buildroot.git
cd buildroot

./configure
make

make install
xenserver-install-wizard
reboot
```

Status by distro
----------------

Some distros get more attention that others and are likely to work better, on average.
Here are the distros which are being actively used:

- Ubuntu-14.04: @djs55
- CentOS 7: @euanh

If you are actively using a distro and feel able to fix bugs in it, please add yourself
to the list.
