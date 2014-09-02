#!/bin/bash

# Configure the local machine to install packages built in this working directory

XAPIBASEURL=${PKG_REPO_LOCATION:-file://$PWD/RPMS/}
XAPISRCBASEURL=${SRC_REPO_LOCATION:-file://$PWD/SRPMS/}

sed \
    -e "s,@XAPIBASEURL@,${XAPIBASEURL},g" \
    -e "s,@XAPISRCBASEURL@,${XAPISRCBASEURL},g" \
    scripts/rpm/xapi.repo.in > scripts/rpm/xapi.repo
install -m 0644 scripts/rpm/xapi.repo /etc/yum.repos.d/xapi.repo

install -m 0644 scripts/rpm/xen-c6.repo /etc/yum.repos.d/xen-c6.repo
#install -m 0644 scripts/rpm/xen-c6-RC1.repo /etc/yum.repos.d/xen-c6-RC1.repo
install -m 0644 scripts/rpm/xen-c6-tweaked.repo /etc/yum.repos.d/home:jonludlam.repo

install -m 0644 scripts/rpm/epel.repo /etc/yum.repos.d/epel.repo

install -m 0644 scripts/rpm/RPM-GPG-KEY-EPEL-6 /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

yum repolist
yum install -y xenserver-core
