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

The definitions for the VM are in the definitions/ directory. The
VM can be built by:

```
veewee vbox build xenserver-62-devel -n
```

Hopefully this succeeds and prints text like the following:
```
The box xenserver-62-devel was built successfully!
You can now login to the box with:
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 7222 -l vagrant 127.0.0.1
```

Building xapi
-------------

All the pre-requesites are installed into the VM. To build xapi, log in
via ssh and execute:

```
git clone git://github.com/xapi-project/xen-api-libs
cd xen-api-libs
git checkout clearwater-sp1-lcm
sh autogen.sh
./configure
make
sudo make install

cd ..
git clone git://github.com/xapi-project/xen-api
cd xen-api
git checkout clearwater-sp1-lcm
make
```

Note the unit tests for xapi fail unless you run them as root.

Using vagrant
-------------

If you wish to use vagrant to repeatedly clone the VM, then first
export as a vagrant 'box':
```
veewee vbox export xenserver-62-devel
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

