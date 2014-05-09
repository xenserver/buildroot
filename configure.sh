#!/bin/bash
set -eu

if [ `lsb_release -si` == "Fedora" -o `lsb_release -si` == "CentOS" -o `lsb_release -si` == "RedHatEnterpriseServer" ] ; then
	. scripts/rpm/configure.sh

elif [ `lsb_release -si` == "Ubuntu" -o `lsb_release -si` == "Debian" -o `lsb_release -si` == "Linaro" ] ; then
	. scripts/deb/configure.sh
fi
