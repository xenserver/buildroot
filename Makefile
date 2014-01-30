-include deps

deps: SPECS/*.spec specdep.py
	@echo Updating dependencies...
	@./specdep.py -i libnl3 SPECS/*.spec > $@

