Using mock to build these RPMs:
==============================

(tidy this up later)

useradd djs -G mock
passwd djs
 
cp xenserver.cfg /etc/mock/

su - djs

mock -r xenserver --init
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-obuild-0.0.2-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/cppo-0.9.3-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/easy-format-1.0.1-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/biniou-1.0.6-0.src.rpm
createrepo RPMS/x86_64

