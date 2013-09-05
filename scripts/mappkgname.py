#!/usr/bin/python

"""Maps an RPM package name to the equivalent DEB.
   The mapping is static, but in future will be 
   made dynamically by querying the package databases."""


def mapPackageBaseName(name):
    """rewrite an rpm name to fit with debian standards"""
    # Debian puts the language name after the library name
    # whereas Fedora puts it before
    if name.startswith( "ocaml-" ):
        name = name[ len("ocaml-"): ] + "-ocaml"

    return name

mapping = { 
    "biniou": "libbiniou-ocaml",
    "cmdliner": "libcmdliner-ocaml",
    "cppo": "cppo",
    "deriving-ocsigen": "libderiving-ocsigen-ocaml",
    "easy-format": "libeasy-format-ocaml",
    "eliloader": "eliloader",
    "ffs": "ffs",
    "forkexecd": "forkexecd",
    "js_of_ocaml": "libjs-of-ocaml",
    "libnl3-cli": "libnl-3-cli",
    "libnl3-doc": "libnl-3-doc",
    "libnl3": "libnl-3",
    "message-switch": "message-switch",
    "ocaml-bitstring": "libbitstring-ocaml",
    "ocaml-camomile-data": "libcamomile-data-ocaml",
    "ocaml-camomile": "libcamomile-ocaml",
    "ocaml-cdrom": "libcdrom-ocaml",
    "ocaml-cohttp": "libcohttp-ocaml",
    "ocaml-cstruct": "libcstruct-ocaml",
    "ocaml-fd-send-recv": "libfd-send-recv-ocaml",
    "ocaml-lambda-term": "liblambda-term-ocaml",
    "ocaml-libvhd": "libvhd-ocaml",
    "ocaml-libvirt": "libvirt-ocaml",
    "ocaml-lwt": "liblwt-ocaml",
    "ocaml-nbd": "libnbd-ocaml",
    "ocaml-netdev": "libnetdev-ocaml",
    "ocaml-obuild": "ocaml-obuild",
    "ocaml-oclock": "liboclock-ocaml" ,
    "ocaml-ocplib-endian": "ocplib-endian-ocaml",
    "ocaml-ounit": "libounit-ocaml",
    "ocaml-qmp": "libqmp-ocaml",
    "ocaml-react": "libreact-ocaml",
    "ocaml-re": "libre-ocaml" ,
    "ocaml-rpc": "librpc-ocaml",
    "ocaml-sexplib": "libsexplib-camlp4",
    "ocaml-ssl": "libssl-ocaml" ,
    "ocaml-stdext": "libstdext-ocaml",
    "ocaml-syslog": "libsyslog-ocaml",
    "ocaml-tapctl": "libtapctl-ocaml",
    "ocaml-text": "libtext-ocaml",
    "ocaml-type-conv": "libtype-conv-camlp4",
    "ocaml-uri": "liburi-ocaml" ,
    "ocaml-uuidm": "libuuidm-ocaml",
    "ocaml-xcp-idl": "libxcp-idl-ocaml",
    "ocaml-xcp-inventory": "libxcp-inventory-ocaml",
    "ocaml-xcp-rrd": "libxcp-rrd-ocaml",
    "ocaml-xen-api-client": "libxen-api-client-ocaml",
    "ocaml-xen-api-libs-transitional": "ocaml-xen-api-libs-transitional",
    "ocaml-xen-lowlevel-libs": "ocaml-xen-lowlevel-libs",
    "ocaml-xenops": "libxenops-ocaml",
    "ocaml-xenstore-clients": "libxenstore-clients-ocaml",
    "ocaml-xenstore": "libxenstore-ocaml",
    "ocaml-yojson": "libyojson-ocaml",
    "ocaml-zed": "libzed-ocaml",
    "omake": "omake",
    "openstack-xapi-plugins": "openstack-xapi-plugins",
    "optcomp": "optcomp-ocaml",
    "sm-cli": "sm-cli",
    "squeezed": "squeezed",
    "utop": "utop",
    "vncterm": "vncterm",
    "xapi-libvirt-storage": "libxapi-libvirt-storage-ocaml",
    "xapi-python": "xapi-python",
    "xapi": "xapi",
    "xapi-xe": "xapi-xe",
    "xcp-networkd": "xcp-networkd" ,
    "xcp-rrdd": "xcp-rrdd",
    "xe-create-templates": "xe-create-templates",
    "xenops-cli": "xenops-cli",
    "xenopsd-libvirt": "xenopsd-libvirt",
    "xenopsd-simulator": "xenopsd-simulator",
    "xenopsd-xc": "xenopsd-xc",
    "xenopsd-xenlight": "xenopsd-xenlight",
    "xenopsd": "xenopsd",
    "xenserver-core": "xenserver-core",
    "xenserver-install-wizard": "xenserver-install-wizard",
    "xenserver-tech-preview-release": "xenserver-tech-preview-release",
    "xmlm": "libxmlm-ocaml",
    "xsconsole": "xsconsole",
    "xsiostat": "xsiostat",
    "xenserver-core-latest-snapshot": "xenserver-core-latest-snapshot",

    # extras
    "ocaml": ["ocaml-nox", "ocaml-native-compilers"],
    "ocaml-findlib": "ocaml-findlib",
    "ocaml-ocamldoc": "ocaml-nox",
    "ocaml-compiler-libs":   # added to ocaml-uri - why does rpmbuild succeed?
                  "ocaml-compiler-libs",
    "ocaml-camlp4": ["camlp4", "camlp4-extra"],
    "openssl": "libssl1.0.0",
    "xen": "xen-hypervisor",
    "libuuid": "uuid",
    "libvirt": ["libvirt0", "libvirt-bin"],
    "xen-libs": "libxen-4.2",
    "make": "make",
    "ncurses": "libncurses5",
    "chkconfig": [], # "chkconfig",
    "initscripts": [], # "initscripts",
    "PyPAM": "python-pam",
    "perl": "perl",
    "gawk": "gawk",
    "pam": "libpam0g",
    "tetex-latex": "texlive-base",
    "zlib": "zlib1g",
    "git": "git",
    "stunnel": "stunnel",
    "bash-completion": "bash-completion",
    "python": "python",
    "time": "time",
    "newt": "libnewt0.52",
    "flex": "flex",
    "bison": "bison",
    "/sbin/ldconfig": "/sbin/ldconfig",
    "kernel-headers": "linux-headers-3.2.0-51-generic",
    "libvirt-docs": "libvirt-doc",
    "chrpath": "chrpath",
    "kernel": "linux-image",
    "kernel-firmware": "linux-firmware",

    # this seems to come from packages like xcp-networkd, which don't have
    # any requirements
    "/bin/sh": "/bin/sh",
    "libxl-headers": "libxl-headers",
    "xen-utils": "xen-utils",
    "nfs-utils": "nfs-common",
    "hwdata": "hwdata",
    "redhat-lsb-core": "lsb-base",
    "ethtool": "ethtool",
    "qemu-system-x86": "qemu-system-x86",
    "python-argparse": "libpython2.7-stdlib",
}

secondary_mapping = {
    "camlp4-dev": "camlp4",
}

def mapPackage(name):
    """map an rpm to a corresponding deb, based on file contents"""
    # XXXXX  for now we use a static map
    isDevel=False
    if name.endswith( "-devel" ):
        isDevel = True
        name = name[ :-len("-devel") ]
    mapped = mapping[name]
    if type(mapped) != list:
       mapped = [mapped]
    res = []
    for m in mapped:
        if isDevel:
            m += "-dev"
        if m == "camlp4-dev":
            m = "camlp4"
        if m == "camlp4-extra-dev":
            m = "camlp4-extra"
        if m == "libeasy-format-ocaml":  # packages with 'ocaml' or 'camlp4' must have a -dev...
            m = "libeasy-format-ocaml-dev"
        if m == "libbiniou-ocaml":  # packages with 'ocaml' or 'camlp4' must have a -dev...
            m = "libbiniou-ocaml-dev"
        if m == "libssl1.0.0-dev":
            m = "libssl-dev"
        if m == "libtype-conv-camlp4":
            m = "libtype-conv-camlp4-dev"
        if m == "libxapi-libvirt-storage-ocaml":
            m = "libxapi-libvirt-storage-ocaml-dev"
        if m == "libsexplib-camlp4":
            m = "libsexplib-camlp4-dev"
        if m == "ocaml-findlib-dev":
            m = ["ocaml-findlib", "libfindlib-ocaml-dev"]
        if m == "/bin/sh":
            continue
        if m == "xen-hypervisor-dev":
            m = ["libxen-dev", "xen-utils", "blktap-dev"]
        if m == "libvirt0-dev":
            m = "libvirt-dev"
        if m == "libxen-4.2-dev":
            m = "libxen-dev"
        if m == "libvirt-bin-dev":
            m = "libvirt-bin"
        if type(m) != list:
           m = [m]
        res += m
    return res


def mapPackageName(hdr):
    """rewrite an rpm name to fit with debian standards"""
    name = hdr['name']
    # XXX UGLY

    # Debian adds a -dev suffix to development packages,
    # whereas Fedora uses -devel
    isDevel = False
    if name.endswith( "-devel" ):
        isDevel = True
        name = name[ :-len("-devel") ]

    #name = mapPackageBaseName(name)

    # Debian prefixes library packag names with 'lib'
    #if "Libraries" in hdr['group'] or "library" in hdr['summary'].lower():
    #    name = "lib" + name

    # Do this manually for now...
    name = name.replace( name, mapPackage(name)[0] )

    if isDevel:
        name += "-dev"

    # hack for type-conv.   dh_ocaml insists that there must be a -dev package for anything with ocaml or camlp4 in the name...
    if name == "libtype-conv-camlp4":
        name = "libtype-conv-camlp4-dev"
    return name

def mapSection(rpm_name):
    return "ocaml" # XXXXX

