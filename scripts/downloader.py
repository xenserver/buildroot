#!/usr/bin/env python

import sys
import urlparse
import os
import subprocess
import time

def guess_file_type(path):
	# If we have python2.7:
	#line = subprocess.check_output(["file", path])
	p = subprocess.Popen(["file", path], stdout = subprocess.PIPE)
	line = p.stdout.read()
	p.communicate()
	if p.returncode <> 0:
		print >>sys.stderr, "file %s: failed with exit code %d" % (path, p.returncode)
		exit(1)
	# file: description
	if len(line) < (len(path) + 2):
		print >>sys.stderr, "Malformed output from 'file %s': '%s'" % (path, line)
		exit(1)
	return line[len(path) + 2:].strip()

def looks_like_an_archive(path):
	ty = guess_file_type(path)
	if ty.startswith("ASCII") or ty.startswith("HTML"):
		return False
	if ty.startswith("gzip") or ty.startswith("bzip"):
		return True
	print >>sys.stderr, "%s has an unrecognised file type: %s" % (path, ty)
	print >>sys.stderr, "Please extend %s:looks_like_an_archive to include this case."
	exit(1)

def download(url, destination):
	args = ["curl", "--silent", "--show-error", "-L", "-o", destination, url]
	print >>sys.stderr, "Running %s" % (" ".join(args))
	returncode = subprocess.call(args)
	if returncode <> 0:
		print >>sys.stderr, "Downloading %s failed: sleeping 5s" % url
		time.sleep(5)

def look_for_it(url, destination):
	for attempt in [5, 4, 3, 2, 1, 0]:
		if os.path.exists(destination):
			if looks_like_an_archive(destination):
				print >>sys.stderr, "%s exists and looks like an archive" % destination
				# Refresh the archive's last access time.
				# If the spec file which depends on this archive has been modified, it will have a later access time than the archive and make will continually rebuild it.   'Touch' the archive, to prevent this happening
				# There is a potential race here:  http://stackoverflow.com/questions/1158076/implement-touch-using-python
				with open(destination, 'a'):
					os.utime(destination, None)
				return
			else:
				print >>sys.stderr, "%s is not an archive, deleting it" % destination
				os.unlink(destination)
				if attempt == 0:
					print >>sys.stderr, "That was our last attempt so giving up."
					exit(1)
		else:
			print >>sys.stderr, "%s does not exist: downloading" % destination
			download(url, destination)

if __name__ == "__main__":
	if len(sys.argv) <> 3:
		print >>sys.stderr, "Wrong number of arguments. Use %s <url> <destination>" % sys.argv[0]
		exit(1)
	url_string = sys.argv[1]
	destination = sys.argv[2]
	url = urlparse.urlparse(url_string)
	path = url.path.split('/')
	# Avoid relying on github to set the destination filename
	if url.netloc == "github.com" and path[-3] == "archive":
		ext = None
		possible_exts = [ ".tar", ".tar.gz", ".zip", ".tbz", "tar.bz2" ]
		for e in possible_exts:
			if url.path.endswith(e):
				ext = e
				break
		if not ext:
			print >>sys.stderr, "I did not recognise extension of %s. I know about: %s" % (url.path, ", ".join(possible_exts))
			exit(1)
		url_path = "/".join(path[0:-2] + [ path[-2] + ext ])
		url_string = str(urlparse.urlunsplit((url.scheme, url.netloc, url_path, url.query, url.fragment),))
	look_for_it(url_string, destination)
