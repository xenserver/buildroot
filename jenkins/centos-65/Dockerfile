FROM            centos:latest
MAINTAINER      Euan Harris <euan.harris@citrix.com>

# Update
RUN     yum upgrade -y

# Install Jenkins requirements
RUN     yum -y install openssh-server
RUN     mkdir /var/run/sshd
RUN     yum -y install java-1.7.0-openjdk

RUN useradd jenkins 
RUN echo "jenkins:jenkins" |chpasswd

# Install EPEL
RUN curl -OL http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN curl -OL http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm

# Install bootstrap dependencies
RUN yum install -y mock redhat-lsb-core rpm-build git augeas sudo

# Mock won't run as root
RUN usermod -G mock,wheel -a jenkins

# Disable 'requiretty' so that build scripts can call sudo
RUN augtool -s set /files/etc/sudoers/Defaults[*]/requiretty/negate ""

# Add jenkins to sudoers.  It's faster to write this file in the docker
# recipe than to add it with 'add' because a rebuild of the image has to
# start at the earliest add - RUNs can be taken from the cache.

RUN echo 'jenkins ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/builder
RUN chown root.root /etc/sudoers.d/builder
RUN chmod 440 /etc/sudoers.d/builder

RUN service sshd start

EXPOSE 22
CMD    /usr/sbin/sshd -D
