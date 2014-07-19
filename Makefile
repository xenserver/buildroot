DIST := .el6
DISTRIBUTION=`lsb_release -si`

.PHONY: all rpms srpms

all: rpms


# RPM build rules

%.src.rpm: 
	@echo [RPMBUILD] $@
	@rpmbuild --quiet --define "_topdir ." --define "%dist $(DIST)" -bs $<
	@echo [CREATEREPO] $@
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
	@mkdir -p logs
	@touch RPMS/Packages	
	@sudo cowbuilder --build \
		--configfile pbuilder/pbuilderrc \
		--buildresult RPMS $<
	@echo [UPDATEREPO] $@
	@flock --timeout 30 ./RPMS scripts/deb/updaterepo packages RPMS


# Dependency build rules

deps: SPECS/*.spec specdep.py scripts/lib/mappkgname.py
	@echo Updating dependencies...
	if [ "$(DISTRIBUTION)" != "CentOS" ]; then \
		@./specdep.py -d $(DIST) -i libnl3 SPECS/*.spec > $@ \
	else \
		@./specdep.py -d $(DIST) SPECS/*.spec > $@ \
	fi

-include deps

