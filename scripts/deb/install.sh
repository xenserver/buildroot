#!/bin/bash -x

DEBURL=${PKG_REPO_LOCATION:-file:$PWD/RPMS/}
DEBSRCURL=${SRC_REPO_LOCATION:-file:$PWD/SRPMS/}

REPOHOST=""
if [[ "$DEBURL" =~ ^http://.* ]]; then
    REPOHOST=$(echo "$DEBURL" | sed -e 's,^http://\([^/]*\)/.*$,\1,g')
fi

# Configure the local machine to install packages built in this workspace
sed \
    -e "s,@DEBURL@,${DEBURL},g" \
    -e "s,@DEBSRCURL@,${DEBSRCURL},g" \
    scripts/deb/xapi.list.in > scripts/deb/xapi.list
install -m 0644 scripts/deb/xapi.list /etc/apt/sources.list.d/xapi.list

# Configure apt to prefer packages from the xenserver-core repository
sed \
    -e "s,@REPOHOST@,${REPOHOST},g" \
    scripts/deb/xapi.pref.in > scripts/deb/xapi.pref
install -m 0644 scripts/deb/xapi.pref /etc/apt/preferences.d/xapi

(mkdir -p RPMS && cd RPMS && apt-ftparchive packages . > Packages)
(mkdir -p SRPMS && cd SRPMS && apt-ftparchive sources . > Sources )

# Install
apt-get update
apt-get install -y --force-yes xenserver-core

