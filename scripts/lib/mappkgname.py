#!/usr/bin/python

import platform

"""Maps an RPM package name to the equivalent DEB.
   The MAPPING is static, but in future will be 
   made dynamically by querying the package databases."""

TARGET_SPECIFIC_MAPPING = {
    'debian:jessie/sid': {
            'kernel': ['linux-image-amd64'],
            'kernel-firmware': ['firmware-linux-free'],
            "xen-libs": ["libxen-4.3"],
            },
    'ubuntu:14.04': {
            "xen-libs": ["libxen-4.4"],
            },
    'linaro:14.04': {
            "xen-libs": ["libxen-4.4"],
            },
    }

MAPPING = { 
    # Our packages
    "ocaml-biniou": ["libbiniou-ocaml"],
    "ocaml-cmdliner": ["libcmdliner-ocaml"],
    "deriving-ocsigen": ["libderiving-ocsigen-ocaml"],
    "ocaml-easy-format": ["libeasy-format-ocaml"],
    "linux-guest-loader": ["linux-guest-loader"],
    "iscsi-initiator-utils": ["open-iscsi"],
    "js_of_ocaml": ["libjs-of-ocaml"],
    "libnl3-cli": ["libnl-cli-3-200"],
    "libnl3-doc": ["libnl-doc"],
    "libnl3": ["libnl-3-200", "libnl-route-3-200"],
    "libffi": ["libffi6"],
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
    "openstack-xapi-plugins": ["openstack-xapi-plugins"],
    "optcomp": ["optcomp-ocaml"],
    "xapi-libvirt-storage": ["libxapi-libvirt-storage-ocaml"],
    "ocaml-xmlm": ["libxmlm-ocaml"],
    "xsconsole0": ["xsconsole"],
    "xenserver-core-latest-snapshot": ["xenserver-core-latest-snapshot"],
    "python-setuptools": ["python-setuptools", "python-setuptools-git"],

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
    "ncurses": ["libncurses5"],
    "chkconfig": [], 
    "initscripts": [], 
    "PyPAM": ["python-pam"],
    "pam": ["libpam0g"],
    "tetex-latex": ["texlive-base"],
    "zlib": ["zlib1g"],
    "stunnel": ["stunnel"],
    "bash-completion": ["bash-completion"],
    "python2": ["python"],
    "newt": ["libnewt0.52"],
    "/sbin/ldconfig": ["/sbin/ldconfig"],
    "kernel-headers": ["linux-headers-3.2.0-51-generic"],
    "libvirt-docs": ["libvirt-doc"],
    "kernel": ["linux-image"],
    "kernel-firmware": ["linux-firmware"],
    "/bin/sh": [],
    "xen-runtime": ["xen-utils"],
    "nfs-utils": ["nfs-common"],
    "redhat-lsb-core": ["lsb-base"],
    "sg3_utils": ["sg3-utils"],
    "python-argparse": ["libpython2.7-stdlib"],
    "util-linux-ng": ["uuid-runtime"],
    "autoconf": ["autoconf"],
    "automake": ["automake"],
}

SECONDARY_MAPPING = {
    "camlp4-dev": ["camlp4"],
    "camlp4-extra-dev": ["camlp4-extra"],
    # packages with 'ocaml' or 'camlp4' in the name must have a -dev...
    "libssl1.0.0-dev": ["libssl-dev"],
    "libtype-conv-camlp4": ["libtype-conv-camlp4-dev"],
    "libxapi-libvirt-storage-ocaml": ["libxapi-libvirt-storage-ocaml-dev"],
    "ocaml-findlib-dev": ["ocaml-findlib", "libfindlib-ocaml-dev"],
    "xen-hypervisor-dev": ["libxen-dev", "blktap-dev"],
    "libvirt0-dev": ["libvirt-dev"],
    "libxen-4.2-dev": ["libxen-dev"],
    "libffi6-dev": ["libffi-dev"],
    "libvirt-bin-dev": ["libvirt-bin"],
    "blktap-utils-dev": ["blktap-utils"],
    "qemu-system-x86-dev": ["qemu-system-x86"],
}

def map_package(name, target=None):
    """map an rpm to a corresponding deb, based on file contents"""
    is_devel = False

    if target is None:
        dist = platform.linux_distribution(full_distribution_name=False)
        target = "%s:%s" % (dist[0].lower(), dist[1].lower())

    # RPM 4.6 adds architecture constraints to dependencies.  Drop them.
    if name.endswith( "(x86-64)" ):
        name = name[ :-len("(x86-64)") ]
    if name.endswith( "-devel" ):
        is_devel = True
        name = name[ :-len("-devel") ]

    default = [name]
    mapped = MAPPING.get(name, default)

    if target in TARGET_SPECIFIC_MAPPING:
        mapped = TARGET_SPECIFIC_MAPPING[target].get(name, mapped)

    res = []
    for debname in mapped:
        if is_devel:
            debname += "-dev"
        res += SECONDARY_MAPPING.get(debname, [debname])
    return res


def map_package_name(hdr, target=None):
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
    name = name.replace( name, map_package(name, target)[0] )

    if is_devel:
        name += "-dev"

    # hack for type-conv.   dh_ocaml insists that there must be a 
    # -dev package for anything with ocaml or camlp4 in the name...
    if name == "libtype-conv-camlp4":
        name = "libtype-conv-camlp4-dev"
    return name

def map_section(_rpm_name):
    return "ocaml" # XXXXX

