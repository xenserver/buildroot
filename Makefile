DIST := .el6

.PHONY: all rpms srpms

all: rpms


# RPM build rules

%.src.rpm: 
	@echo [RPMBUILD] $@
	@rpmbuild --quiet --define "_topdir ." --define "%dist $(DIST)" -bs $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./SRPMS

%.rpm:
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir=$(dir $@) --rebuild $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS


# Deb build rules

%.dsc: 
	@echo [MAKEDEB] $@
	@scripts/deb/makedeb.py $<
	@echo [APT-FTPARCHIVE] $@
	@cd ./SRPMS && apt-ftparchive sources . > Sources

%.deb:
	@echo [COWBUILDER] $@
	@sudo cowbuilder --build \
		--configfile pbuilder/pbuilderrc \
		--buildresult RPMS $<
	@echo [APT-FTPARCHIVE] $@
	@cd ./RPMS && apt-ftparchive packages . > Packages



# Dependency build rules

deps: SPECS/*.spec specdep.py scripts/lib/mappkgname.py
	@echo Updating dependencies...
	@./specdep.py -d $(DIST) -i libnl3 SPECS/*.spec > $@

-include deps
