#!/bin/bash
set -eu

# Check we can use sudo, so the rest of the script can run as any user
which sudo > /dev/null || ( [ `id -u` == "0" ] && apt-get install sudo ) || echo "Please install sudo"
sudo /bin/true || echo "Please configure sudo for current user"

if [ `lsb_release -si` == "Fedora" -o `lsb_release -si` == "CentOS" -o `lsb_release -si` == "RedHatEnterpriseServer" ] ; then
	. scripts/rpm/configure.sh

elif [ `lsb_release -si` == "Ubuntu" -o `lsb_release -si` == "Debian" -o `lsb_release -si` == "Linaro" ] ; then
	. scripts/deb/configure.sh
fi
