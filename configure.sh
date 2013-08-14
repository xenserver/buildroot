#!/bin/sh

ARCH=amd64
DIST=raring
BASETGZ=/var/cache/pbuilder/base-$DIST-$ARCH.tgz

apt-get install pbuilder

echo -n "Writing pbuilder configuration..."
mkdir -p pbuilder
sed -e "s|@PWD@|$PWD|g" -e "s|@ARCH@|$ARCH|g" -e "s|@BASETGZ@|$BASETGZ|g" -e "s|@DIST@|$DIST|g" pbuilderrc.in > pbuilder/pbuilderrc-$DIST-$ARCH
sed -e "s|@PWD@|$PWD|g" D05deps.in > pbuilder/D05deps
chmod 755 pbuilder/D05deps
echo " done"

if [ -f $BASETGZ ] ; then
    echo $BASETGZ exists - updating
    sudo pbuilder --update --override-config --configfile $PWD/pbuilder/pbuilderrc-$DIST-$ARCH
else
    echo $BASETGZ does not exist - creating
    sudo pbuilder --create --configfile $PWD/pbuilder/pbuilderrc-$DIST-$ARCH
fi

echo -n "Initializing repository..."
mkdir -p RPMS SRPMS
(cd RPMS; apt-ftparchive packages . > Packages)
(cd SRPMS; apt-ftparchive sources . > Sources)
echo " done"

