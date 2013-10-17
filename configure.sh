#!/bin/bash
set -eu

if [ `lsb_release -si` == "Fedora" -o `lsb_release -si` == "CentOS" ] ; then
	. scripts/rpm/configure.sh

elif [ `lsb_release -si` == "Ubuntu" -o `lsb_release -si` == "Debian" ] ; then
	. scripts/deb/configure.sh
fi
