#!/bin/bash
set -eu

echo "Configuring RPM-based build"
DISTRIBUTION=`lsb_release -si`
case "$DISTRIBUTION" in
    Fedora)
        DISTNAME="fedora"
        DISTRELEASE=`rpm --eval %{?fedora}`
        ;;

    CentOS|RedHatEnterpriseServer)
        DISTNAME="el"
        DISTRELEASE=`rpm --eval %{?rhel}`
        ;;

    *)
        echo "Unknown distribution: $DISTRIBUTION"
        exit 1
        ;;
esac

PLANEX_REPO_RPM="https://xenserver.github.io/planex-release/rpm/${DISTNAME}/planex-release-${DISTRELEASE}-1.noarch.rpm"
rpm -q planex-release >/dev/null 2>&1 || sudo yum install -y $PLANEX_REPO_RPM
sudo yum -y install planex

echo -n "Writing mock configuration..."
mkdir -p mock
sed -e "s|@PWD@|$PWD|g" scripts/rpm/mock-default.cfg.in > mock/default.cfg
for i in Xen4CentOS ocaml-4.01 ; do
    echo >> mock/default.cfg
    cat scripts/rpm/$i.repo >> mock/default.cfg
done
echo '"""' >> mock/default.cfg

ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
echo " done"
