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
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-yojson-1.1.6-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/cmdliner-0.9.3-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-ounit-1.1.2-3.el6.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-qmp-0.9.0-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/optcomp-1.4-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-ocplib-endian-0.3-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-cstruct-0.7.1-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-cdrom-0.9.1-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-re-1.2.1-0.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-uri-1.3.8-0.src.rpm
createrepo RPMS/x86_64
