DIST := .el6

.PHONY: all rpms srpms srpm_repo

all: rpms


############################################################################
# RPM build rules
############################################################################

# Build a source RPM from a Spec file and a tarball.   We define %dist
# to ensure that the names of the source RPMs, which are built outside the
# mock chroot, match the names of the binary RPMs, which are built inside
# the chroot.	Without this we might generate foo-1.0.fc20.src.rpm
# (Fedora host) and foo-1.0.el6.x86_64.rpm (CentOS chroot).
%.src.rpm:
	@echo [RPMBUILD] $@ 
	@rpmbuild --quiet --define "_topdir ." \
		--define "%dist $(DIST)" -bs $<

# Phony target to create repository metadata for the SRPMs.   This makes
# it possible to add the SRPMS directory to yum.conf and use yumdownloader
# to install source RPMs.
srpm_repo: srpms
	echo [CREATEREPO] SRPMS
	@flock --timeout 30 ./SRPMS createrepo --quiet --update ./SRPMS

# Build one or more binary RPMs from a source RPM.   A typical source RPM
# might produce a base binary RPM, a -devel binary RPM containing library
# and header files and a -debuginfo binary RPM containing debug symbols.
# The repository metadata is updated after building a binary package so that
# a subsequent mock build for a package which depend on this one is able
# to find and install it.
%.rpm:
	@echo [MOCK] $@
	@mock --configdir=mock --quiet \
		--resultdir=$(dir $@) --uniqueext=$(notdir $@) --rebuild $<
	@echo [CREATEREPO] $@
	@flock --timeout 30 ./RPMS createrepo --quiet --update ./RPMS


############################################################################
# Deb build rules
############################################################################

# Build a Debian source package from a Spec file and a tarball.
# makedeb.py loads the Spec file, generates an equivalent Debian source
# directory structure, then runs 'dpkg-source' to create the .dsc file.
# The conversion is basic, but works fairly well for straightforward Spec
# files.
%.dsc: 
	@echo [MAKEDEB] $@
	@scripts/deb/makedeb.py $<
	@echo [UPDATEREPO] $@
	@flock --timeout 30 ./SRPMS scripts/deb/updaterepo sources SRPMS

# Build one or more binary Debian packages from from a source package.
# As with the RPM build, a typical source package might produce several
# binary packages.  The repository metadata is updated after building a
# binary package so that a subsequent build for a package which depends
# on this one is able to find and install it.
%.deb:
	@echo [COWBUILDER] $@
	@touch RPMS/Packages
	@sudo cowbuilder --build \
		--configfile pbuilder/pbuilderrc \
		--buildresult RPMS $<
	@echo [UPDATEREPO] $@
	@flock --timeout 30 ./RPMS scripts/deb/updaterepo packages RPMS


############################################################################
# Dependency build rules
############################################################################

# Generate dependency rules linking spec files to tarballs, source
# packages and binary packages.   specdep.py generates rules suitable
# for RPM or Debian builds depending on the host distribution.
deps: SPECS/*.spec specdep.py scripts/lib/mappkgname.py
	@echo Updating dependencies...
	@./specdep.py -d $(DIST) --ignore-from ignore SPECS/*.spec > $@

-include deps

