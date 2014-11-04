#!/bin/bash
set -eu

# Each distribution comes with a different set of existing
# packages.
rm -f ignore
VERSION=`lsb_release -si`.`lsb_release -sc`
IGNORE=ignore.$VERSION
echo Looking for a file called $IGNORE
if [ -e $IGNORE ]; then
  ln -s $IGNORE ignore
else
  ln -s ignore.default ignore
fi

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
