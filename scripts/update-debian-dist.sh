#!/bin/sh

rm -rf dists
mkdir -p dists/raring/main/binary-amd64
mkdir -p dists/raring/main/binary-i386
mkdir -p dists/raring/main/source

rsync --delete -avu SRPMS/* dists/raring/main/source
rsync --delete -avu RPMS/*.deb dists/raring/main/binary-amd64

cat >dists/raring/main/binary-amd64/Release <<EOF
Archive: raring
Version: 13.04
Component: main
Origin: Citrix
Label: XenServer Core
Architecture: amd64
EOF

cat >dists/raring/main/source/Release <<EOF
Archive: raring
Version: 13.04
Component: main
Origin: Citrix
Label: XenServer Core
Architecture: source
EOF

# Sometimes we get the wrong sizes in the packages file
# http://www.linuxquestions.org/questions/blog/bittner-195120/howto-build-your-own-debian-repository-2863/
#apt-ftparchive generate apt-raring-release.conf
#apt-ftparchive -c apt-raring-release.conf packages dists/raring/main >dists/raring/main/binary-amd64/Packages
#apt-ftparchive -c apt-raring-release.conf release dists/raring/ >dists/raring/Release


# https://enc.com.au/2007/08/07/creating-an-apt-archive/
apt-ftparchive generate scripts/archive.conf

echo "now run: rsync -avu --delete dists/ ~/public_html/dists/"
