#!/bin/sh

rm -rf dists
mkdir -p dists/trusty/main/binary-amd64
mkdir -p dists/trusty/main/binary-i386
mkdir -p dists/trusty/main/source

rsync --delete -avu SRPMS/* dists/trusty/main/source
rsync --delete -avu RPMS/*.deb dists/trusty/main/binary-amd64

cat >dists/trusty/main/binary-amd64/Release <<EOF
Archive: trusty 
Version: 13.04
Component: main
Origin: Citrix
Label: XenServer Core
Architecture: amd64
EOF

cat >dists/trusty/main/source/Release <<EOF
Archive: trusty
Version: 13.04
Component: main
Origin: Citrix
Label: XenServer Core
Architecture: source
EOF

# Sometimes we get the wrong sizes in the packages file
# http://www.linuxquestions.org/questions/blog/bittner-195120/howto-build-your-own-debian-repository-2863/
#apt-ftparchive generate apt-trusty-release.conf
#apt-ftparchive -c apt-trusty-release.conf packages dists/trusty/main >dists/trusty/main/binary-amd64/Packages
#apt-ftparchive -c apt-trusty-release.conf release dists/trusty/ >dists/trusty/Release


# https://enc.com.au/2007/08/07/creating-an-apt-archive/
apt-ftparchive generate scripts/deb/archive.conf

echo "now run: rsync -avu --delete dists/ ~/public_html/dists/"
