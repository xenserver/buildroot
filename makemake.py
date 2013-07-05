#!/usr/bin/python

# see http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch16s04.html

import rpm
import os
import urlparse

# for debugging, make all paths relative to PWD
rpm.addMacro( '_topdir', '.' )

rpm_dir = rpm.expandMacro( '%_rpmdir' )
spec_dir = rpm.expandMacro( '%_specdir' )
srpm_dir = rpm.expandMacro( '%_srcrpmdir' )
src_dir = rpm.expandMacro( '%_sourcedir' )

print "all: rpms"

rpmfilenamepat = rpm.expandMacro( '%_build_name_fmt' )

ts = rpm.TransactionSet()

def specFromFile( spec ):
    return rpm.ts().parseSpec( spec )

spec_names = os.listdir( spec_dir )
specs = {}
for s in spec_names:
    specs[s] = specFromFile( os.path.join( spec_dir, s ) )

def srpmNameFromSpec( spec ):
    h = spec.sourceHeader
    rpm.addMacro( 'NAME', h['name'] )
    rpm.addMacro( 'VERSION', h['version'] )
    rpm.addMacro( 'RELEASE', h['release'] )
    rpm.addMacro( 'ARCH', 'src' )

    # There doesn't seem to be a macro for the name of the source
    # rpm, but the name appears to be the same as the rpm name format.
    # Unfortunately expanding that macro gives us a leading 'src' that we
    # don't want, so we strip that off

    srpmname = os.path.basename( rpm.expandMacro( rpmfilenamepat ) )  
    rpm.delMacro( 'NAME' )
    rpm.delMacro( 'VERSION' )
    rpm.delMacro( 'RELEASE' )
    rpm.delMacro( 'ARCH' )
    return srpmname

# Rules to build SRPM from SPEC
rule_spec_from_srpm = 'rpmbuild -bs $<'
for specname, spec in specs.iteritems():
    srpmname = srpmNameFromSpec( spec )
    sources = [ os.path.join( src_dir, p ) for p in spec.sourceHeader['source'] ]
    patches = [ os.path.join( src_dir, p ) for p in spec.sourceHeader['patch'] ]

    print '%s: %s %s %s' % (os.path.join( srpm_dir, srpmname ), 
                         os.path.join( spec_dir, specname ),
                         " ".join( sources ),
                         " ".join( patches ) )
    print '\t%s' % rule_spec_from_srpm

def rpmNamesFromSpec( spec ):
    def rpmNameFromHeader( h ):
        rpm.addMacro( 'NAME', h['name'] )
        rpm.addMacro( 'VERSION', h['version'] )
        rpm.addMacro( 'RELEASE', h['release'] )
        rpm.addMacro( 'ARCH', h['arch'] )
        rpmname = rpm.expandMacro( rpmfilenamepat )
        rpm.delMacro( 'NAME' )
        rpm.delMacro( 'VERSION' )
        rpm.delMacro( 'RELEASE' )
        rpm.delMacro( 'ARCH' )
        return rpmname
    return [rpmNameFromHeader( p.header ) for p in spec.packages]
    
# Rules to download sources

# Assumes each RPM only needs one download - we have some multi-source
# packages but in all cases the additional sources are patches provided
# in the Git repository
for specname, spec in specs.iteritems():
    # The RPM documentation says that RPM only cares about the basename
    # of the path given in a Source: tag.   spec.sourceHeader['url'] 
    # enforces this - even if we have a URL in the source tag, it 
    # will only give us the basename.   However the full tag text is
    # available in spec.sources.   It's not clear whether or not we
    # can rely on this as part of the RPM library API.

    for (source, _, _) in spec.sources:
	url = urlparse.urlparse( source )
	if url.scheme is not "":
            print '%s: %s' % ( 
		os.path.join( src_dir, os.path.basename( url.path ) ),
		os.path.join( spec_dir, specname ) )
            print '\tcurl -L -o $@ %s' % source
    

# Rules to build RPMS from SRPMS (uses information from the SPECs to
# get packages)
for specname, spec in specs.iteritems():
    # This doesn't generate the right Makefile fragment for a multi-target
    # rule - we may end up building too often, or not rebuilding correctly
    # on a partial build
    rpmnames = rpmNamesFromSpec( spec )
    srpmname = srpmNameFromSpec( spec )
    for r in rpmnames: 
        rpm_path = os.path.join( rpm_dir, r )
        srpm_path = os.path.join( srpm_dir, srpmname )
        rpm_outdir = os.path.dirname( rpm_path )
        print '%s: %s' % ( rpm_path, srpm_path )
        print '\tmock -r xenserver --resultdir="%s" $<' % rpm_outdir
        print '\tcreaterepo --update %s' % rpm_dir
        
# RPM build dependencies.   The 'requires' key for the *source* RPM is
# actually the 'buildrequires' key from the spec
def buildRequiresFromSpec( spec ):
    return spec.sourceHeader['requires']

provides_to_rpm = {}
for specname, spec in specs.iteritems():
    for package in spec.packages:
        for provided in (package.header['provides'] + [package.header['name']]):
            for rpmname in rpmNamesFromSpec( spec ):
                provides_to_rpm[ provided ] = rpmname

for specname, spec in specs.iteritems():
    for rpmname in rpmNamesFromSpec( spec ):
        for buildreq in buildRequiresFromSpec( spec ):
            # Some buildrequires come from the system repository
            if provides_to_rpm.has_key( buildreq ):
                buildreqrpm = provides_to_rpm[buildreq]
                print "%s: %s" % (os.path.join( rpm_dir, rpmname ), 
                                  os.path.join( rpm_dir, buildreqrpm ) )


# Generate targets to build all srpms and all rpms
all_srpms = [ os.path.join( srpm_dir, srpmNameFromSpec( s ) ) 
              for s in specs.values() ]

all_rpms = []
for rpms in [ rpmNamesFromSpec( s ) for s in specs.values() ]:
    all_rpms += map( (lambda rpm: os.path.join( rpm_dir, rpm )), rpms )


print "rpms: " + " \\\n\t".join( all_rpms )
print "srpms: " + " \\\n\t".join( all_srpms )
