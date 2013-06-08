#!/bin/sh

sed "s|@HOME@|$HOME|" xenserver.cfg.in > xenserver.cfg
