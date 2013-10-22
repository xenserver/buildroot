-include deps


./SRPMS/%.src.rpm: 
	@echo [RPMBUILD] $@
	@rpmbuild --quiet --define "_topdir ." -bs $<


./SRPMS/%.dsc: 
	@echo [MAKEDEB] $@
	scripts/deb/makedeb.py $<


./RPMS/x86_64/%.x86_64.rpm: ./SRPMS/%.src.rpm
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir="./RPMS/x86_64" $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS


./RPMS/noarch/%.noarch.rpm: ./SRPMS/%.src.rpm
	@echo [MOCK] $@
	@mock --configdir=mock --quiet -r xenserver --resultdir="./RPMS/noarch" $<
	@echo [CREATEREPO] $@
	@createrepo --quiet --update ./RPMS


./RPMS/%_amd64.deb: ./SRPMS/%.dsc
	@echo [COWBUILDER] $@
	sudo cowbuilder --build --configfile pbuilder/pbuilderrc-raring-amd64 --buildresult ./RPMS $<


deps: SPECS/*.spec makemake.py
	./makemake.py > $@

