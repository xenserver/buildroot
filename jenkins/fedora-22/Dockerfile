FROM            fedora:22
MAINTAINER      Euan Harris <euan.harris@citrix.com>

# This fails because of the following problem:
#   https://bugzilla.redhat.com/show_bug.cgi?format=multiple&id=1171928

# Update
RUN     dnf upgrade -y

# Install Jenkins requirements
RUN     dnf -y install openssh-server
RUN     mkdir /var/run/sshd
RUN     dnf -y install java-1.8.0-openjdk-headless

RUN useradd jenkins 
RUN echo "jenkins:jenkins" |chpasswd

# Install extra repositories
RUN dnf -y install epel-release

# Install bootstrap dependencies
RUN dnf install -y mock redhat-lsb-core rpm-build git augeas sudo

# Mock won't run as root
RUN usermod -G mock,wheel -a jenkins

# Disable 'requiretty' so that build scripts can call sudo
RUN augtool -s set /files/etc/sudoers/Defaults[*]/requiretty/negate ""

# Disable privilege separation in ssh
# http://stackoverflow.com/questions/25428669/connect-via-ssh-to-jhipster-docker-container-on-centos-7
RUN augtool -s set /files/etc/ssh/sshd_config/UsePrivilegeSeparation no
RUN sshd-keygen

# Add jenkins to sudoers.  It's faster to write this file in the docker
# recipe than to add it with 'add' because a rebuild of the image has to
# start at the earliest add - RUNs can be taken from the cache.

RUN echo 'jenkins ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/builder
RUN chown root.root /etc/sudoers.d/builder
RUN chmod 440 /etc/sudoers.d/builder

EXPOSE 22
CMD    /usr/sbin/sshd -D
