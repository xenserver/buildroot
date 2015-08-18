#!/bin/bash

# Configure the local machine to install packages built in this working directory


XAPIBASEURL=${PKG_REPO_LOCATION:-file://$PWD/RPMS/}
XAPISRCBASEURL=${SRC_REPO_LOCATION:-file://$PWD/SRPMS/}

sed \
    -e "s,@XAPIBASEURL@,${XAPIBASEURL},g" \
    -e "s,@XAPISRCBASEURL@,${XAPISRCBASEURL},g" \
    scripts/rpm/xapi.repo.in > scripts/rpm/xapi.repo

for i in xapi CentOS-Xen ; do
    install -m 0644 scripts/rpm/$i.repo /etc/yum.repos.d/$i.repo
done

yum update -y
yum -y install epel-release

yum repolist
yum install -y xenserver-core
