#!/bin/bash
set -eu

echo "Configuring RPM-based build"

DEPS="mock rpm-build createrepo python-argparse"
rpm -q $DEPS >/dev/null 2>&1 || sudo yum install -y $DEPS

echo -n "Writing mock configuration..."
mkdir -p mock
sed -e "s|@PWD@|$PWD|g" scripts/rpm/xenserver.cfg.in > mock/xenserver.cfg
ln -fs /etc/mock/default.cfg mock/
ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
echo " done"
