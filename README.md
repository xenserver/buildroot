Tools to create a build environment for XenServer 6.2, capable of building
the [xapi toolstack](https://github.com/xapi-project/xen-api).

Requirements
------------

The environment will be a virtual machine created by
[veewee](https://github.com/jedi4ever/veewee),
cloned by [vagrant](http://www.vagrantup.com/)
and hosted by any vagrant-supported hypervisor
such as [virtual box](http://virtualbox.org/).

Building the environment
------------------------

The definitions for the VM are in the definitions/ directory. THe
VM can be built by:

```
veewee vbox build xenserver-62-devel -n
```

This will take a while and create a file 'xenserver-62-devel.box'.
Next, import this into vagrant:

```
vagrant box add xenserver-62-devel xenserver-62-devel.box 
```

Now you can create instances of this as follows:

```
mkdir test
cd test
vagrant init xenserver-62-devel
vagrant up
vagrant ssh
```

Building xapi
-------------

All the pre-requesites are installed into the VM. To build xapi:

```
vagrant ssh

git clone git://github.com/xapi-project/xen-api-libs
cd xen-api-libs
git checkout clearwater
sh autogen.sh
./configure
make
sudo make install

cd ..
git clone git://github.com/xapi-project/xen-api
cd xen-api
make
```

