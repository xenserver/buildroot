Using mock to build these RPMs:
==============================

(tidy this up later)

```
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
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-react-0.9.4-0.el6.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir=./RPMS/%(target_arch)s/ SRPMS/ocaml-text-0.6-0.el6.src.rpm
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-cohttp-0.9.8-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/xmlm-1.1.1-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-syslog-1.4-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-bitstring-2.0.4-0.el6.src.rpm createrepo RPMS/x86_64
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-oclock-0.3-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-nbd-0.9.0-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/omake-0.9.8.6-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-type-conv-109.20.00-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/deriving-ocsigen-0.3c-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/js_of_ocaml-1.3.2-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-rpc-1.4.1-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-ssl-0.4.6-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-xenstore-1.2.1-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/message-switch-0.9.2-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-fd-send-recv-1.0.1-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-xcp-idl-0.9.1-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-uuidm-0.9.5-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/xenops-cli-0.9.0-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/sm-cli-0.9.0-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-stdext-0.9.0-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/forkexec-0.9.0-0.src.rpm 
createrepo RPMS/x86_64
mock -r xenserver --resultdir="./RPMS/%(target_arch)s/" SRPMS/ocaml-xen-lowlevel-libs-0.9.0-0.src.rpm
createrepo RPMS/x86_64
```
