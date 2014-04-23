#!/bin/bash

cat > /etc/yum.repos.d/xenserver-62-devel.repo <<EOT
[xenserver-62-devel]
name=xenserver-62-devel
baseurl=http://dave.recoil.org/xenserver-62-devel/el5/RPMS
gpgcheck=0
EOT


# add EPEL
rpm -Uvh http://dl.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
yum repolist

#  
# install dependencies
yum groupinstall -y 'Development Tools'
yum install -y git libev-devel blktap-devel automake ocaml-omake pam-devel zlib zlib-devel ocaml-bitstring-devel ocaml-camlp4 ocaml-findlib ocaml-findlib-devel ocaml-getopt ocaml-getopt-devel ocaml-lwt ocaml-lwt-devel ocaml-obus ocaml-obus-devel ocaml-ounit ocaml-ounit-devel ocaml-react ocaml-react-devel ocaml-text ocaml-text-devel ocaml-type-conv ocaml-xmlm ocaml-xmlm-devel xen-devel

