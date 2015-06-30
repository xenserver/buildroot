#!/bin/bash

docker build --rm=true --force-rm=true --tag=jenkins-centos-6.5 centos-65
docker build --rm=true --force-rm=true --tag=jenkins-centos-7.0 centos-70
docker build --rm=true --force-rm=true --tag=jenkins-fedora-21 fedora-21
docker build --rm=true --force-rm=true --tag=jenkins-fedora-22 fedora-22
docker build --rm=true --force-rm=true --tag=jenkins-fedora-rawhide fedora-rawhide

docker build --rm=true --force-rm=true --tag=jenkins-ubuntu-14.04 ubuntu-1404
docker build --rm=true --force-rm=true --tag=jenkins-debian-jessie debian-jessie

