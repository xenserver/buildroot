#!/bin/bash -x

# Add the OCaml 4 PPA
install -m 0644 scripts/deb/ocp-ppa.list /etc/apt/sources.list.d/ocp-ppa.list

# Add the xen-4.3 PPA
install -m 0644 scripts/deb/xenbits-xen-4.3.list /etc/apt/sources.list.d/xenbits-xen-4.3.list

# Configure the local machine to install packages built in this workspace
sed -e "s,@PWD@,$PWD,g" scripts/deb/xapi.list.in > scripts/deb/xapi.list
install -m 0644 scripts/deb/xapi.list /etc/apt/sources.list.d/xapi.list

# Configure apt to prefer packages from the local repository
install -m 0644 scripts/deb/xapi.preference /etc/apt/preferences.d/xapi

# Install
apt-get update
apt-get install -y xenserver-core

