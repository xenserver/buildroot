#!/bin/bash
set -eu

if [ `lsb_release -si` == "Fedora" -o `lsb_release -si` == "CentOS" ] ; then

	echo "Configuring RPM-based build"

	rpm -q mock rpm-build >/dev/null 2>&1 || sudo yum install -y mock rpm-build

	echo -n "Writing mock configuration..."
	mkdir -p mock
	sed "s|@PWD@|$PWD|" xenserver.cfg.in > mock/xenserver.cfg
	ln -fs /etc/mock/default.cfg mock/
	ln -fs /etc/mock/site-defaults.cfg mock/
	ln -fs /etc/mock/logging.ini mock/
	echo " done"

	echo -n "Initializing repository..."
	mkdir -p RPMS
	createrepo --quiet RPMS
	echo " done"

elif [ `lsb_release -si` == "Ubuntu" ] ; then

	echo "Configuring DEB-based build"

	ARCH=amd64
	DIST=raring
	BASETGZ=/var/cache/pbuilder/base-$DIST-$ARCH.tgz

	dpkg -l pbuilder python-rpm curl ocaml-nox > /dev/null 2>&1 || sudo apt-get install pbuilder python-rpm curl ocaml-nox
	mkdir -p BUILD

	echo -n "Writing pbuilder configuration..."
	mkdir -p pbuilder
	sed -e "s|@PWD@|$PWD|g" -e "s|@ARCH@|$ARCH|g" -e "s|@BASETGZ@|$BASETGZ|g" -e "s|@DIST@|$DIST|g" pbuilderrc.in > pbuilder/pbuilderrc-$DIST-$ARCH
	sed -e "s|@PWD@|$PWD|g" D05deps.in > pbuilder/D05deps
	chmod 755 pbuilder/D05deps
	echo " done"

	echo -n "Initializing repository..."
	mkdir -p RPMS SRPMS
	(cd RPMS; apt-ftparchive packages . > Packages)
	(cd SRPMS; apt-ftparchive sources . > Sources)
        echo " done"

	if [ -f $BASETGZ ] ; then
	    echo $BASETGZ exists - updating
	    sudo pbuilder --update --override-config --configfile $PWD/pbuilder/pbuilderrc-$DIST-$ARCH
	else
	    echo $BASETGZ does not exist - creating
	    sudo pbuilder --create --configfile $PWD/pbuilder/pbuilderrc-$DIST-$ARCH
            # inject Keyfile for Launchpad PPA for Louis Gesbert
            sudo pbuilder --execute --configfile $PWD/pbuilder/pbuilderrc-$DIST-$ARCH --save-after-exec -- /usr/bin/apt-key add - << KEYFILE
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.4
Comment: Hostname: keyserver.ubuntu.com

mI0EUgJE5QEEANHD2l6yuvqffhqTcJd4nOQVax6m9i4SKb/IpXqOh40PYzG17bc0rbGaM7CU
+nD9vDAtP6Wjjc5aatMyYOQ1aPzAmPtFfvjg9NyR88r9GK7G8sR6N2YzarUblrxI0yEmfc9X
409JOejfgv7s1D/Jmsoo5GqYQihXiSBS7juJk6ihABEBAAG0H0xhdW5jaHBhZCBQUEEgZm9y
IExvdWlzIEdlc2JlcnSIuAQTAQIAIgUCUgJE5QIbAwYLCQgHAwIGFQgCCQoLBBYCAwECHgEC
F4AACgkQrWm///0xBNZrugQAqEz0xu6FmNSvCtn9vVghI8/UAoYla87qHSjEY1gmQ9oC4/0Y
hPh2pBmI475HlPvESksjApsUHh9ksc9SkLiNS9rPE5rFp/gEDjFA6arFcaPcNmAu51x3lDfh
KQ3afU1hlF6EsITRd5qGry7ftxoLKOrVp8qSw9O/PdFgBTTGvgE=
=ZOqF
-----END PGP PUBLIC KEY BLOCK-----
KEYFILE
            # inject Keyfile for Launchpad PPA for Anil Madhavapeddy
            sudo pbuilder --execute --configfile $PWD/pbuilder/pbuilderrc-$DIST-$ARCH --save-after-exec -- /usr/bin/apt-key add - << KEYFILE
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.4
Comment: Hostname: keyserver.ubuntu.com

mI0EUd0+wQEEAMOeX/cGrgub9dEn9xjViAQub7w94JhGYKEpS2w79N3nQKA5NLBxpwvwH9xb
R7tjVJ11g/feZ+xKkbtcDNHc+BW8IpKf4x7qPy1JrDZ0c8KQhGA6TJY61Wgg4Rwzzi9l1n7L
G+EkIPotbHY0D27zqzFqwIKj+SbJFPZ9Ty1Z2VCLABEBAAG0I0xhdW5jaHBhZCBQUEEgZm9y
IEFuaWwgTWFkaGF2YXBlZGR5iLgEEwECACIFAlHdPsECGwMGCwkIBwMCBhUIAgkKCwQWAgMB
Ah4BAheAAAoJEFstDFVhcHsJryAD/01EFC2zz8LjmEvJX3hPBkkDipD+NCPsuxe78H1QR7AV
MLzqar1aYcQk/zVUGJDdIcbJnHJ2OnyeeJ0wOVOmJKSrch+jePUkLzM3bWdx5fbK5b4o2nYW
Xp9mmv8bABlmMr5PDd6/G9y5HTBeImUe7v6a4EtFnF3LnBY0Nkmh9QGq
=4ul6
-----END PGP PUBLIC KEY BLOCK-----
KEYFILE

	fi

	echo " done"

fi
