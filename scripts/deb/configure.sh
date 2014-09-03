#!/bin/bash
set -eu

echo "Configuring DEB-based build"

if [ $(arch | grep arm) ]; then
  echo Running on an $(arch) so targetting armhf
  ARCH=${ARCH:-armhf}
else
  echo Running on an $(arch) so targetting amd64
  ARCH=${ARCH:-amd64}
fi
DIST=${DIST:-`lsb_release -sc`}
BASEPATH=/var/cache/pbuilder/base.cow
APT_REPOS=${APT_REPOS:-}
DEFAULT_MIRROR=$(grep "^deb .*$DIST .*main" /etc/apt/sources.list | cut -d' ' -f 2 | head -n1)
MIRROR=${MIRROR:-$DEFAULT_MIRROR}

if [ `lsb_release -si` == "Ubuntu" ] ; then
    APT_REPOS="$APT_REPOS |deb $MIRROR $DIST universe"
fi
if [ $ARCH == 'armhf' ]; then
    APT_REPOS="$APT_REPOS |deb $MIRROR $DIST restricted universe"
fi

dpkg -l cowbuilder python-rpm curl ocaml-nox apt-utils gdebi-core software-properties-common > /dev/null 2>&1 || \
   sudo apt-get install cowbuilder python-rpm curl ocaml-nox apt-utils gdebi-core software-properties-common
mkdir -p BUILD

echo -n "Writing pbuilder configuration..."
mkdir -p pbuilder
for file in scripts/deb/templates/*; do
    filename=`basename $file`
    cp $file pbuilder/${filename}
    for replace_var in "APT_REPOS" "PWD" "ARCH" "BASEPATH" "DIST" "MIRROR" ; do
	sed -i -e "s~@$replace_var@~${!replace_var}~g" pbuilder/${filename}
    done
    chmod 755 pbuilder/${filename}
done

echo " done"

echo -n "Initializing repository..."
mkdir -p RPMS SRPMS
(cd RPMS; rm -f Packages; apt-ftparchive packages . > Packages)
(cd SRPMS; rm -f Sources; apt-ftparchive sources . > Sources)
echo " done"

if [ -e $BASEPATH ] ; then
    echo $BASEPATH exists - updating
    sudo cowbuilder --update --override-config --configfile $PWD/pbuilder/pbuilderrc
else
    echo $BASEPATH does not exist - creating
    sudo cowbuilder --create --configfile $PWD/pbuilder/pbuilderrc
    sudo cowbuilder --update --override-config --configfile $PWD/pbuilder/pbuilderrc
fi
echo " done"

