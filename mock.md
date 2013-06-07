Using mock to build these RPMs:
==============================

(tidy this up later)

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
