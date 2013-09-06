import rpm

def filesFromSpec(basename, specpath):
    """The RPM library doesn't seem to give us access to the files section,
    so we need to go and get it ourselves.   This parsing algorithm is
    based on build/parseFiles.c in RPM.   The list of section titles
    comes from build/parseSpec.c.   We should get this by using ctypes
    to load the rpm library."""
    """XXX shouldn't be parsing this by hand.   will need to handle conditionals
    within and surrounding files and packages sections."""

    #XXX Why do we need the .install.in files?

    otherparts = [ 
        "%package", 
        "%prep", 
        "%build", 
        "%install", 
        "%check", 
        "%clean", 
        "%preun", 
        "%postun", 
        "%pretrans", 
        "%posttrans", 
        "%pre", 
        "%post", 
        "%changelog", 
        "%description", 
        "%triggerpostun", 
        "%triggerprein", 
        "%triggerun", 
        "%triggerin", 
        "%trigger", 
        "%verifyscript", 
        "%sepolicy", 
    ]

    files = {}
    with open(specpath) as spec:
        inFiles = False
        section = ""
        for line in spec:
            tokens = line.strip().split(" ")
            if tokens and tokens[0].lower() == "%files":
                section = basename
                inFiles = True
                if len(tokens) > 1:
                    section = basename + "-" + tokens[1]
                continue
                
            if tokens and tokens[0] in otherparts:
                inFiles = False

            if inFiles:
                if tokens[0].lower().startswith("%defattr"):
                    continue
                if tokens[0].lower().startswith("%attr"):
                    continue
                if tokens[0].lower() == "%doc":
                    docsection = section + "-doc"
                    files[docsection] = files.get(docsection, []) + tokens[1:]
                    continue
                if tokens[0].lower() == "%if" or tokens[0].lower() == "%endif":
                    # XXX evaluate the if condition and do the right thing here
                    continue
                if tokens[0].lower() == "%exclude":
                    excludesection = section + "-%exclude"
                    files[excludesection] = files.get(excludesection, []) + tokens[1:]
                    continue
                if tokens[0].lower().startswith("%config"):
                    # dh_install automatically considers files in /etc to be config files 
                    # so we don't have to do anythin special for them
                    # The spec file documentation says that a %config directive can
                    # only apply to a single file.
                    configsection = section + "-%config"
                    if tokens[1].startswith("/etc"):
                        files[section] = files.get(section, []) + tokens[1:]
                    else:
                        files[configsection] = files.get(configsection, []) + tokens[1:]
                    continue
                if line.strip():
                    files[section] = files.get(section, []) + [line.strip()]
        return files
            
