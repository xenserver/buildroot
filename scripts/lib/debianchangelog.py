from tree import Tree
import mappkgname
import re
import time

def changelog_from_spec(spec, isnative):
    res = Tree()

    hdr = spec.sourceHeader
    log = ""
    for (name, timestamp, text) in zip(hdr['changelogname'], 
                                       hdr['changelogtime'], 
                                       hdr['changelogtext']):

        # A Debian package's version is defined by the version of the
        # first entry in the changelog, so we must get this right.
        # Most spec files have changelog entries starting "First Last
        # <first@foo.com> - version" - this seems to be the standard
        # for Red Hat spec files.
        # Some of our changelos only have "First Last <first@foo.com>".   
        # For these, we use the version from the spec. 
        match = re.match( "^(.+) - (\S+)$", name )
        if match:
            author = match.group(1)
            version = match.group(2)
            if isnative:
                version = re.sub('-', '.', version)
        else:
            author = name
            sep = '.' if isnative else '-'
            version = "%s%s%s" % (spec.sourceHeader['version'],
                                  sep,
                                  spec.sourceHeader['release'])
        print version

        package_name = mappkgname.map_package(hdr['name'])[0]
        log += "%s (%s) UNRELEASED; urgency=low\n" % (package_name, version)
        log += "\n"

        text = re.sub( "^-", "*", text, flags=re.MULTILINE )
        text = re.sub( "^", "  ", text, flags=re.MULTILINE )
        log += "%s\n" % text
        log += "\n"

        date_string =  time.strftime("%a, %d %b %Y %H:%M:%S %z", 
                                     time.gmtime(int(timestamp)))
        log += " -- %s  %s\n" % (author, date_string)
        log += "\n"

    res.append('debian/changelog', log)
    return res

