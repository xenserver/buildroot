#!/bin/bash

# Configure the local machine to install packages built in this working directory

# May need to update before we install epel over https
yum update -y

XAPIBASEURL=${PKG_REPO_LOCATION:-file://$PWD/RPMS/}
XAPISRCBASEURL=${SRC_REPO_LOCATION:-file://$PWD/SRPMS/}

sed \
    -e "s,@XAPIBASEURL@,${XAPIBASEURL},g" \
    -e "s,@XAPISRCBASEURL@,${XAPISRCBASEURL},g" \
    scripts/rpm/xapi.repo.in > scripts/rpm/xapi.repo

for i in xapi Xen4CentOS ocaml-4.01
do
    install -m 0644 scripts/rpm/$i.repo /etc/yum.repos.d/$i.repo
done

yum -y install epel-release

yum repolist
yum install -y xenserver-core
