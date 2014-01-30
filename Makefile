DIST := .el6

.PHONY: all rpms srpms

all: rpms


# RPM build rules

%.src.rpm: 
	@echo [RPMBUILD] $@
	@rpmbuild --quiet --define "_topdir ." --define "%dist $(DIST)" -bs $<

%.x86_64.rpm:
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir="RPMS/x86_64" $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS

%.noarch.rpm:
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir="RPMS/noarch" $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS


# Deb build rules

%.dsc: 
	@echo [MAKEDEB] $@
	@scripts/deb/makedeb.py $<

%.deb:
	@echo [COWBUILDER] $@
	@sudo cowbuilder --build \
		--configfile pbuilder/pbuilderrc-raring-amd64 \
		--buildresult RPMS $<


# Dependency build rules

deps: SPECS/*.spec specdep.py
	@echo Updating dependencies...
	@./specdep.py -i libnl3 SPECS/*.spec > $@

-include deps
