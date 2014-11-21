FROM            ubuntu:14.04
MAINTAINER      Euan Harris <euan.harris@citrix.com>

# Update
RUN     apt-get -y update
RUN     apt-get -y dist-upgrade

# Install Jenkins requirements
RUN     apt-get -y install openssh-server
RUN     mkdir /var/run/sshd
RUN     service ssh start
RUN     apt-get -y install default-jre-headless

RUN     useradd jenkins
RUN     echo "jenkins:jenkins" |chpasswd
RUN     mkdir -p /home/jenkins
RUN     chown jenkins:jenkins /home/jenkins

# Install bootstrap dependencies
RUN     apt-get -y install git augeas-tools sudo lsb-release

# Disable 'requiretty' so that build scripts can call sudo
RUN     augtool -s set /files/etc/sudoers/Defaults[*]/requiretty/negate ""

RUN     apt-get -y --force-yes install ocaml-nox

# Make apt assume -y (needed for ./configure.sh)
RUN     echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90-assume-yes
RUN     echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf.d/90-assume-yes

# Add jenkins to sudoers.  It's faster to write this file in the docker
# recipe than to add it with 'add' because a rebuild of the image has to
# start at the earliest add - RUNs can be taken from the cache.

RUN     echo 'jenkins ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/builder
RUN     chown root.root /etc/sudoers.d/builder
RUN     chmod 440 /etc/sudoers.d/builder

EXPOSE  22
CMD     /usr/sbin/sshd -D
