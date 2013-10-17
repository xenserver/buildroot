#!/bin/bash
set -eu

echo "Configuring RPM-based build"

rpm -q mock rpm-build >/dev/null 2>&1 || sudo yum install -y mock rpm-build

echo -n "Writing mock configuration..."
mkdir -p mock
sed "s|@PWD@|$PWD|" xenserver.cfg.in > mock/xenserver.cfg
ln -fs /etc/mock/default.cfg mock/
ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
echo " done"

echo -n "Initializing repository..."
mkdir -p RPMS
createrepo --quiet RPMS
mkdir -p SRPMS
echo " done"

