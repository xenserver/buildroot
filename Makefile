-include deps

deps: SPECS/*.spec
	./makemake.py > $@

