#!/bin/bash -x

# Add the OCaml 4 PPA
install -m 0644 scripts/deb/ocp-ppa.list /etc/apt/sources.list.d/ocp-ppa.list

DEBURL=${PKG_REPO_LOCATION:-file:$PWD/RPMS/}
DEBSRCURL=${SRC_REPO_LOCATION:-file:$PWD/SRPMS/}

# Configure the local machine to install packages built in this workspace
sed \
    -e "s,@DEBURL@,${DEBURL},g" \
    -e "s,@DEBSRCURL@,${DEBSRCURL},g" \
    scripts/deb/xapi.list.in > scripts/deb/xapi.list
install -m 0644 scripts/deb/xapi.list /etc/apt/sources.list.d/xapi.list

# Configure apt to prefer packages from the local repository
install -m 0644 scripts/deb/xapi.pref /etc/apt/preferences.d/xapi

(cd RPMS && apt-ftparchive packages . > Packages)
(cd SRPMS && apt-ftparchive sources . > Sources )

# Install
apt-get update
apt-get install -y --force-yes xenserver-core

