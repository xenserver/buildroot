#!/bin/bash

docker build --rm=true --force-rm=true --tag=jenkins-centos-6.5 centos-65
docker build --rm=true --force-rm=true --tag=jenkins-ubuntu-14.04 ubuntu-1404
docker build --rm=true --force-rm=true --tag=jenkins-debian-jessie debian-jessie

