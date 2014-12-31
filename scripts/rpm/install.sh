#!/bin/bash

# Configure the local machine to install packages built in this working directory

XAPIBASEURL=${PKG_REPO_LOCATION:-file://$PWD/RPMS/}
XAPISRCBASEURL=${SRC_REPO_LOCATION:-file://$PWD/SRPMS/}

sed \
    -e "s,@XAPIBASEURL@,${XAPIBASEURL},g" \
    -e "s,@XAPISRCBASEURL@,${XAPISRCBASEURL},g" \
    scripts/rpm/xapi.repo.in > scripts/rpm/xapi.repo
install -m 0644 scripts/rpm/xapi.repo /etc/yum.repos.d/xapi.repo

install -m 0644 scripts/rpm/centos-xen-4-4.repo /etc/yum.repos.d/centos-xen-4-4.repo

yum -y install epel-release

yum repolist
yum install -y xenserver-core
