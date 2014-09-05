DIST := .el6

.PHONY: all rpms srpms

all: rpms

clean:
	[ ! -e srpm_output.log ] || rm srpm_output.log
	[ ! -e rpm_output.log ] || rm rpm_output.log
	[ ! -e deps ] || rm deps
	rm -rf RPMS SRPMS

SRPMS/.stamp:
	mkdir -p SRPMS
	createrepo --quiet SRPMS
	touch $@

RPMS/.stamp:
	mkdir -p RPMS
	createrepo --quiet RPMS
	touch $@

# RPM build rules

%.src.rpm: SRPMS/.stamp
	@echo [RPMBUILD] $@
	@rpmbuild --define "_topdir ." --define "%dist $(DIST)" -bs $(word 2,$^) >> srpm_output.log 2>&1
	@echo [CREATEREPO] $@
	@scripts/runonce_queue.sh SRPMS 30 $@ createrepo --update ./SRPMS >> srpm_output.log 2>&1

%.rpm: RPMS/.stamp
	@echo [MOCK] $@
	@mock --configdir=mock -r xenserver --resultdir=$(dir $@) --uniqueext=$(notdir $@) --rebuild $(word 2,$^) >> rpm_output.log 2>&1
	@echo [CREATEREPO] $@
	@scripts/runonce_queue.sh RPMS 30 $@ createrepo --update ./RPMS >> rpm_output.log 2>&1


# Deb build rules

%.dsc: 
	@echo [MAKEDEB] $@
	@scripts/deb/makedeb.py $< >> srpm_output.log 2>&1
	@echo [UPDATEREPO] $@
	@scripts/runonce_queue.sh SRPMS 30 $@ scripts/deb/updaterepo sources SRPMS >> srpm_output.log 2>&1

%.deb:
	@echo [COWBUILDER] $@
	@mkdir -p logs
	@touch RPMS/Packages	
	@sudo cowbuilder --build \
		--configfile pbuilder/pbuilderrc \
		--buildresult RPMS $< >> rpm_output.log 2>&1
	@echo [UPDATEREPO] $@
	@scripts/runonce_queue.sh RPMS 30 $@ scripts/deb/updaterepo packages RPMS >> rpm_output.log 2>&1


# Dependency build rules

deps: SPECS/*.spec specdep.py scripts/lib/mappkgname.py
	@echo Updating dependencies...
	@./specdep.py -d $(DIST) --ignore-from ignore SPECS/*.spec > $@

-include deps

