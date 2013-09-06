#!/usr/bin/python

"""Maps an RPM package name to the equivalent DEB.
   The MAPPING is static, but in future will be 
   made dynamically by querying the package databases."""


MAPPING = { 
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
    "xcp-sm": "xcp-sm",
    "sm-cli": "sm-cli",
    "xcp-sm-rawhba": "xcp-sm-rawhba",
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
    "xen": ["xen-hypervisor", "qemu-system-x86", "blktap-utils"],
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
    "swig": "swig",

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

SECONDARY_MAPPING = {
    "camlp4-dev": "camlp4",
}

def map_package(name):
    """map an rpm to a corresponding deb, based on file contents"""
    is_devel = False
    if name.endswith( "-devel" ):
        is_devel = True
        name = name[ :-len("-devel") ]
    mapped = MAPPING[name]
    if type(mapped) != list:
        mapped = [mapped]
    res = []
    for newname in mapped:
        if is_devel:
            newname += "-dev"
        if newname == "camlp4-dev":
            newname = "camlp4"
        if newname == "camlp4-extra-dev":
            newname = "camlp4-extra"
        # packages with 'ocaml' or 'camlp4' must have a -dev...
        if newname == "libeasy-format-ocaml":  
            newname = "libeasy-format-ocaml-dev"
        if newname == "libbiniou-ocaml":
            newname = "libbiniou-ocaml-dev"
        if newname == "libssl1.0.0-dev":
            newname = "libssl-dev"
        if newname == "libtype-conv-camlp4":
            newname = "libtype-conv-camlp4-dev"
        if newname == "libxapi-libvirt-storage-ocaml":
            newname = "libxapi-libvirt-storage-ocaml-dev"
        if newname == "libsexplib-camlp4":
            newname = "libsexplib-camlp4-dev"
        if newname == "ocaml-findlib-dev":
            newname = ["ocaml-findlib", "libfindlib-ocaml-dev"]
        if newname == "/bin/sh":
            continue
        if newname == "xen-hypervisor-dev":
            newname = ["libxen-dev", "xen-utils", "blktap-dev"]
        if newname == "libvirt0-dev":
            newname = "libvirt-dev"
        if newname == "libxen-4.2-dev":
            newname = "libxen-dev"
        if newname == "libvirt-bin-dev":
            newname = "libvirt-bin"
        if newname == "blktap-utils-dev":
            newname = "blktap-utils"
        if newname == "qemu-system-x86-dev":
            newname = "qemu-system-x86"
        if type(newname) != list:
            newname = [newname]
        res += newname 
    return res


def map_package_name(hdr):
    """rewrite an rpm name to fit with debian standards"""
    name = hdr['name']
    # XXX UGLY

    # Debian adds a -dev suffix to development packages,
    # whereas Fedora uses -devel
    is_devel = False
    if name.endswith( "-devel" ):
        is_devel = True
        name = name[ :-len("-devel") ]

    # Debian prefixes library packag names with 'lib'
    #if "Libraries" in hdr['group'] or "library" in hdr['summary'].lower():
    #    name = "lib" + name
    name = name.replace( name, map_package(name)[0] )

    if is_devel:
        name += "-dev"

    # hack for type-conv.   dh_ocaml insists that there must be a 
    # -dev package for anything with ocaml or camlp4 in the name...
    if name == "libtype-conv-camlp4":
        name = "libtype-conv-camlp4-dev"
    return name

def map_section(_rpm_name):
    return "ocaml" # XXXXX

