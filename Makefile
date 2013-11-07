-include deps

deps: SPECS/*.spec specdep.py
	@echo Updating dependencies...
	@./specdep.py > $@

