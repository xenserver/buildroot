#!/bin/sh

mkdir -p mock
sed "s|@PWD@|$PWD|" xenserver.cfg.in > mock/xenserver.cfg
ln -fs /etc/mock/default.cfg mock/
ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
