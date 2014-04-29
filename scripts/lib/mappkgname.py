#!/usr/bin/python

"""Maps an RPM package name to the equivalent DEB.
   The MAPPING is static, but in future will be 
   made dynamically by querying the package databases."""


MAPPING = { 
    # Our packages
    "ocaml-biniou": ["libbiniou-ocaml"],
    "ocaml-cmdliner": ["libcmdliner-ocaml"],
    "cppo": ["cppo"],
    "deriving-ocsigen": ["libderiving-ocsigen-ocaml"],
    "ocaml-easy-format": ["libeasy-format-ocaml"],
    "eliloader": ["eliloader"],
    "linux-guest-loader": ["linux-guest-loader"],
    "xcp-python-libs": ["xcp-python-libs"],
    "ffs": ["ffs"],
    "forkexecd": ["forkexecd"],
    "iscsi-initiator-utils": ["open-iscsi"],
    "js_of_ocaml": ["libjs-of-ocaml"],
    "libnl3-cli": ["libnl-3-cli"],
    "libnl3-doc": ["libnl-3-doc"],
    "libnl3": ["libnl-3"],
    "libffi": ["libffi6"],
    "message-switch": ["message-switch"],
    "ocaml-bitstring": ["libbitstring-ocaml"],
    "ocaml-camomile-data": ["libcamomile-data"],
    "ocaml-camomile": ["libcamomile-ocaml"],
    "ocaml-cdrom": ["libcdrom-ocaml"],
    "ocaml-cohttp": ["libcohttp-ocaml"],
    "ocaml-cstruct": ["libcstruct-ocaml"],
    "ocaml-ctypes": ["libctypes-ocaml"],
    "ocaml-crc": ["libcrc-ocaml"],
    "ocaml-fd-send-recv": ["libfd-send-recv-ocaml"],
    "ocaml-gnt": ["libgnt-ocaml"],
    "ocaml-lambda-term": ["liblambda-term-ocaml"],
    "ocaml-libvhd": ["libvhd-ocaml"],
    "ocaml-libvirt": ["libvirt-ocaml"],
    "ocaml-lwt": ["liblwt-ocaml"],
    "ocaml-nbd": ["libnbd-ocaml"],
    "ocaml-netdev": ["libnetdev-ocaml"],
    "ocaml-obuild": ["ocaml-obuild"],
    "ocaml-oclock": ["liboclock-ocaml"],
    "ocaml-ocplib-endian": ["ocplib-endian-ocaml"],
    "ocaml-ounit": ["libounit-ocaml"],
    "ocaml-opasswd": ["libopasswd-ocaml"],
    "ocaml-qmp": ["libqmp-ocaml"],
    "ocaml-react": ["libreact-ocaml"],
    "ocaml-re": ["libre-ocaml"],
    "ocaml-rpc": ["librpc-ocaml"],
    "ocaml-rrd-transport": ["librrd-transport-ocaml"],
    "ocaml-sexplib": ["libsexplib-camlp4"],
    "ocaml-ssl": ["libssl-ocaml"],
    "ocaml-stdext": ["libstdext-ocaml"],
    "ocaml-tapctl": ["libtapctl-ocaml"],
    "ocaml-text": ["libtext-ocaml"],
    "ocaml-type-conv": ["libtype-conv-camlp4"],
    "ocaml-uri": ["liburi-ocaml"],
    "ocaml-uuidm": ["libuuidm-ocaml"],
    "ocaml-xcp-idl": ["libxcp-idl-ocaml"],
    "ocaml-xcp-inventory": ["libxcp-inventory-ocaml"],
    "ocaml-xcp-rrd": ["libxcp-rrd-ocaml"],
    "ocaml-xen-api-client": ["libxen-api-client-ocaml"],
    "ocaml-xen-api-libs-transitional": ["ocaml-xen-api-libs-transitional"],
    "ocaml-xen-lowlevel-libs": ["ocaml-xen-lowlevel-libs"],
    "ocaml-xenops": ["libxenops-ocaml"],
    "ocaml-xenstore-clients": ["libxenstore-clients-ocaml"],
    "ocaml-xenstore": ["libxenstore-ocaml"],
    "ocaml-yojson": ["libyojson-ocaml"],
    "ocaml-zed": ["libzed-ocaml"],
    "ocaml-vhd": ["vhd-ocaml"],
    "ocaml-tar": ["tar-ocaml"],
    "ocaml-uutf": ["uutf-ocaml"],
    "ocaml-odn": ["libodn-ocaml"],
    "ocaml-fileutils": ["libfileutils-ocaml"],
    "ocaml-io-page": ["libio-page-ocaml"],
    "ocaml-sha": ["libsha-ocaml"],
    "ocaml-ipaddr": ["libipaddr-ocaml"],
    "ocaml-mirage-types": ["libmirage-types-ocaml"],
    "omake": ["omake"],
    "ocamlmod": ["ocamlmod"],
    "ocamlify": ["ocamlify"],
    "oasis": ["oasis"],
    "openstack-xapi-plugins": ["openstack-xapi-plugins"],
    "optcomp": ["optcomp-ocaml"],
    "xcp-sm": ["xcp-sm"],
    "sm-cli": ["sm-cli"],
    "xcp-sm-rawhba": ["xcp-sm-rawhba"],
    "squeezed": ["squeezed"],
    "utop": ["utop"],
    "vncterm": ["vncterm"],
    "xapi-libvirt-storage": ["libxapi-libvirt-storage-ocaml"],
    "xapi-python": ["xapi-python"],
    "xapi": ["xapi"],
    "xapi-xe": ["xapi-xe"],
    "xcp-networkd": ["xcp-networkd"],
    "xcp-rrdd": ["xcp-rrdd"],
    "xe-create-templates": ["xe-create-templates"],
    "xenops-cli": ["xenops-cli"],
    "xenopsd-libvirt": ["xenopsd-libvirt"],
    "xenopsd-simulator": ["xenopsd-simulator"],
    "xenopsd-xc": ["xenopsd-xc"],
    "xenopsd-xenlight": ["xenopsd-xenlight"],
    "xenopsd": ["xenopsd"],
    "xenserver-core": ["xenserver-core"],
    "xenserver-install-wizard": ["xenserver-install-wizard"],
    "xenserver-tech-preview-release": ["xenserver-tech-preview-release"],
    "xmlm": ["libxmlm-ocaml"],
    "xsconsole": ["xsconsole"],
    "xsconsole0": ["xsconsole"],
    "xsiostat": ["xsiostat"],
    "xenserver-core-latest-snapshot": ["xenserver-core-latest-snapshot"],
    "python-setuptools": ["python-setuptools", "python-setuptools-git"],
    "vhd-tool": ["vhd-tool"],
    "blktap": ["blktap"],

    # Distribution packages
    "ocaml": ["ocaml-nox", "ocaml-native-compilers"],
    "ocaml-findlib": ["ocaml-findlib"],
    "ocaml-ocamldoc": ["ocaml-nox"],
    "ocaml-compiler-libs": ["ocaml-compiler-libs"],
    "ocaml-camlp4": ["camlp4", "camlp4-extra"],
    "openssl": ["libssl1.0.0"],
    "xen": ["xen-hypervisor", "qemu-system-x86", "blktap-utils"],
    "libuuid": ["uuid"],
    "libvirt": ["libvirt0", "libvirt-bin"],
    "xen-libs": ["libxen-4.2"],
    "make": ["make"],
    "ncurses": ["libncurses5"],
    "chkconfig": [], 
    "initscripts": [], 
    "PyPAM": ["python-pam"],
    "perl": ["perl"],
    "gawk": ["gawk"],
    "pam": ["libpam0g"],
    "tetex-latex": ["texlive-base"],
    "zlib": ["zlib1g"],
    "git": ["git"],
    "stunnel": ["stunnel"],
    "bash-completion": ["bash-completion"],
    "python": ["python"],
    "python2": ["python"],
    "time": ["time"],
    "newt": ["libnewt0.52"],
    "flex": ["flex"],
    "bison": ["bison"],
    "/sbin/ldconfig": ["/sbin/ldconfig"],
    "kernel-headers": ["linux-headers-3.2.0-51-generic"],
    "libvirt-docs": ["libvirt-doc"],
    "chrpath": ["chrpath"],
    "kernel": ["linux-image"],
    "kernel-firmware": ["linux-firmware"],
    "swig": ["swig"],
    "/bin/sh": [],
    "xen-utils": ["xen-utils"],
    "xen-runtime": ["xen-utils"],
    "nfs-utils": ["nfs-common"],
    "hwdata": ["hwdata"],
    "redhat-lsb-core": ["lsb-base"],
    "sg3_utils": ["sg3-utils"],
    "ethtool": ["ethtool"],
    "qemu-system-x86": ["qemu-system-x86"],
    "python-argparse": ["libpython2.7-stdlib"],
    "autoconf": ["autoconf"],
    "automake": ["automake"],
    "libtool": ["libtool"],
    "libaio": ["libaio"],
}

SECONDARY_MAPPING = {
    "camlp4-dev": ["camlp4"],
    "camlp4-extra-dev": ["camlp4-extra"],
    # packages with 'ocaml' or 'camlp4' in the name must have a -dev...
    "libssl1.0.0-dev": ["libssl-dev"],
    "libtype-conv-camlp4": ["libtype-conv-camlp4-dev"],
    "libxapi-libvirt-storage-ocaml": ["libxapi-libvirt-storage-ocaml-dev"],
    "ocaml-findlib-dev": ["ocaml-findlib", "libfindlib-ocaml-dev"],
    "xen-hypervisor-dev": ["libxen-dev", "xen-utils", "blktap-dev"],
    "libvirt0-dev": ["libvirt-dev"],
    "libxen-4.2-dev": ["libxen-dev"],
    "libffi6-dev": ["libffi-dev"],
    "libvirt-bin-dev": ["libvirt-bin"],
    "blktap-utils-dev": ["blktap-utils"],
    "qemu-system-x86-dev": ["qemu-system-x86"],
}

def map_package(name):
    """map an rpm to a corresponding deb, based on file contents"""
    is_devel = False

    # RPM 4.6 adds architecture constraints to dependencies.  Drop them.
    if name.endswith( "(x86-64)" ):
        name = name[ :-len("(x86-64)") ]
    if name.endswith( "-devel" ):
        is_devel = True
        name = name[ :-len("-devel") ]
    mapped = MAPPING[name]
    res = []
    for debname in mapped:
        if is_devel:
            debname += "-dev"
        res += SECONDARY_MAPPING.get(debname, [debname])
    return res


def map_package_name(hdr):
    """rewrite an rpm name to fit with debian standards"""
    name = hdr['name']

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

