#!/bin/bash
set -eu

DISTRIBUTION=`lsb_release -si`
case "$DISTRIBUTION" in
    Fedora|CentOS|RedHatEnterpriseServer)
        . scripts/rpm/configure.sh
        ;;

    Ubuntu|Debian|Linaro)
	. scripts/deb/configure.sh
        ;;

    *)
        echo "Unknown distribution: $DISTRIBUTION"
        exit 1
        ;;
esac
