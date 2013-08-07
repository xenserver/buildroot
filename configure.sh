#!/bin/sh

echo -n "Writing mock configuration..."
mkdir -p mock
sed "s|@PWD@|$PWD|g" xenserver.cfg.in > mock/xenserver.cfg
ln -fs /etc/mock/default.cfg mock/
ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
echo " done"

echo -n "Initializing repository..."
mkdir -p RPMS
createrepo --quiet RPMS
echo " done"

mkdir -p pbuilder

ARCH=amd64
BASETGZ=/var/cache/pbuilder/base-$ARCH.tgz

sed -e "s|@PWD@|$PWD|g" -e "s|@ARCH@|$ARCH|g" -e "s|@BASETGZ@|$BASETGZ|g" pbuilderrc.in > pbuilder/pbuilderrc-$ARCH
sed -e "s|@PWD@|$PWD|g" D05deps.in > pbuilder/D05deps
chmod 755 pbuilder/D05deps

if [ -f $BASETGZ ] ; then
    echo $BASETGZ exists - updating
    sudo pbuilder --update --override-config --configfile $PWD/pbuilder/pbuilderrc-$ARCH
else
    echo $BASETGZ exists - creating
    sudo pbuilder --create --configfile $PWD/pbuilder/pbuilderrc-$ARCH
fi
