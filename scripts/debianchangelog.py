from tree import Tree
import mappkgname
import re
import time

def changelog_from_spec(spec):
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
        m = re.match( "^(.+) - (\S+)$", name )
        if m:
            author = m.group(1)
            version = m.group(2)
        else:
            author = name
            version = "%s-%s" % (spec.sourceHeader['version'], 
                                 spec.sourceHeader['release'])

        package_name = mappkgname.mapPackage(hdr['name'])[0]
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

