#!/bin/sh

URL=dscott@drall.uk.xensource.com:public_html/xapi/

rm -f RPMS/x86_64/*.log
rm -f RPMS/x86_64/*_pkgs
createrepo SRPMS
mkdir -p debug/x86_64
mv RPMS/x86_64/*-debuginfo-*rpm debug/x86_64
createrepo RPMS/x86_64
createrepo debug/x86_64

rsync -avrz --delete xapi.repo RPMS debug SRPMS $URL
