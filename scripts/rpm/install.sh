#!/bin/bash

# Configure the local machine to install packages built in this working directory

XAPIBASEURL=${XAPIBASEURL:-file://$PWD/RPMS/}
XAPISRCBASEURL=${XAPISRCBASEURL:-file://$PWD/SRPMS/}

sed \
    -e "s,@XAPIBASEURL@,${XAPISRCBASEURL},g" \
    -e "s,@XAPISRCBASEURL@,${XAPISRCBASEURL},g" \
    scripts/rpm/xapi.repo.in > scripts/rpm/xapi.repo
install -m 0644 scripts/rpm/xapi.repo /etc/yum.repos.d/xapi.repo

#install -m 0644 scripts/rpm/xen-c6.repo /etc/yum.repos.d/xen-c6.repo
#install -m 0644 scripts/rpm/xen-c6-RC1.repo /etc/yum.repos.d/xen-c6-RC1.repo
install -m 0644 scripts/rpm/xen-c6-tweaked.repo /etc/yum.repos.d/xen-c6-tweaked.repo

install -m 0644 scripts/rpm/epel.repo /etc/yum.repos.d/epel.repo
install -m 0644 scripts/rpm/epel-testing.repo /etc/yum.repos.d/epel-testing.repo
install -m 0644 scripts/rpm/remi.repo /etc/yum.repos.d/remi.repo

install -m 0644 scripts/rpm/RPM-GPG-KEY-EPEL-6 /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
install -m 0644 scripts/rpm/RPM-GPG-KEY-remi /etc/pki/rpm-gpg/RPM-GPG-KEY-remi

yum repolist
yum install -y xenserver-core
