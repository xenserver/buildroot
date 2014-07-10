#!/bin/bash
set -eu

echo "Configuring RPM-based build"

rpm -q mock rpm-build createrepo python-argparse >/dev/null 2>&1 || sudo yum install -y mock rpm-build createrepo python-argparse

echo -n "Writing mock configuration..."
mkdir -p mock
sed -e "s|@PWD@|$PWD|g" scripts/rpm/xenserver.cfg.in > mock/xenserver.cfg
ln -fs /etc/mock/default.cfg mock/
ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
mkdir -p mock/cache
mkdir -p mock/root
chgrp mock mock/cache
chgrp mock mock/root
echo " done"

echo -n "Initializing repository..."
mkdir -p RPMS
createrepo --quiet RPMS
mkdir -p SRPMS
createrepo --quiet SRPMS
echo " done"

