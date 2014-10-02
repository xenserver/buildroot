DIST := .el6

.PHONY: all rpms srpms srpm_repo

all: rpms srpm_repo

# RPM build rules

%.src.rpm: 
	@echo [RPMBUILD] $@
	@rpmbuild --quiet --define "_topdir ." --define "%dist $(DIST)" -bs $<

srpm_repo: srpms
	echo [CREATEREPO] SRPMS
	@flock --timeout 30 ./SRPMS createrepo --quiet --update ./SRPMS

%.rpm:
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir=$(dir $@) --uniqueext=$(notdir $@) --rebuild $<
	@echo [CREATEREPO] $@
	@flock --timeout 30 ./RPMS createrepo --quiet --update ./RPMS



# Deb build rules

%.dsc: 
	@echo [MAKEDEB] $@
	@scripts/deb/makedeb.py $<
	@echo [UPDATEREPO] $@
	@flock --timeout 30 ./SRPMS scripts/deb/updaterepo sources SRPMS

%.deb:
	@echo [COWBUILDER] $@
	@touch RPMS/Packages
	@sudo cowbuilder --build \
		--configfile pbuilder/pbuilderrc \
		--buildresult RPMS $<
	@echo [UPDATEREPO] $@
	@flock --timeout 30 ./RPMS scripts/deb/updaterepo packages RPMS


# Dependency build rules

deps: SPECS/*.spec specdep.py scripts/lib/mappkgname.py
	@echo Updating dependencies...
	@./specdep.py -d $(DIST) --ignore-from ignore SPECS/*.spec > $@

-include deps

