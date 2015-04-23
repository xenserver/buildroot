#!/bin/bash
set -eu

DISTRIBUTION=`lsb_release -si`
case "$DISTRIBUTION" in
    Fedora|CentOS|RedHatEnterpriseServer)
        . scripts/rpm/install.sh
        ;;

    Ubuntu|Debian|Linaro)
	. scripts/deb/install.sh
        ;;

    *)
        echo "Unknown distribution: $DISTRIBUTION"
        exit 1
        ;;
esac
