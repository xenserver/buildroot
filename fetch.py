#!/usr/bin/env python

import os.path, sys
from subprocess import call

SOURCES="./SOURCES"

number_skipped = 0
number_fetched = 0

def fetch(url, override):
	global number_skipped, number_fetched
	final_name = url.split("/")[-1]
	if override <> "":
		final_name = override
	final_path = os.path.join(SOURCES, final_name)
	if os.path.exists(final_path):
		number_skipped = number_skipped + 1
	else:
		print "fetching %s -> %s" % (url, final_path)
		call(["curl", "-L", "-o", final_path, url])
		number_fetched = number_fetched + 1

if __name__ == "__main__":
	if not(os.path.exists(SOURCES)):
		print >>sys.stderr, "SOURCES dir doesn't exist: %s" % SOURCES
		exit(1)
	f = open("sources.csv", "r")
	lines = f.readlines()
	f.close()
	for line in lines:
		line = line.strip()
		if line == "":
			continue
		if line.startswith('#'):
			continue
		url, override = line.split(",")
		fetch(url, override)
	print "number of packages skipped: %d" % number_skipped
	print "number of packages fetched: %d" % number_fetched
