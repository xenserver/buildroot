#!/bin/sh

mkdir mock
sed "s|@HOME@|$HOME|" xenserver.cfg.in > mock/xenserver.cfg
ln -s /etc/mock/default.cfg mock/
ln -s /etc/mock/site-defaults.cfg mock/
ln -s /etc/mock/logging.ini mock/
