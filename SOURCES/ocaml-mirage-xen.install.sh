#!/bin/sh

set -e
set -x

# The make install target in mirage-platform doesn't yet support DESTDIR so
# we perform a manual install.

cd xen
export OCAMLFIND_DESTDIR=$1
echo Installing into $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/mirage-xen
# Why does ocamlfind ignore me and delete that directory??
MIRAGE_OS=xen ./cmd install
mkdir -p $OCAMLFIND_DESTDIR/mirage-xen
if [ -e $2/mirage-xen ]; then
  cp $2/mirage-xen/* $OCAMLFIND_DESTDIR/mirage-xen
fi
find . -name "*.a" -exec cp {} $1/mirage-xen \;
cp _build/runtime/kernel/libxen.a $1/mirage-xen
cp _build/runtime/kernel/longjmp.o $1/mirage-xen
cp _build/runtime/kernel/x86_64.o $1/mirage-xen
cp _build/runtime/kernel/mirage-x86_64.lds $1/mirage-xen

