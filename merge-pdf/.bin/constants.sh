#! /bin/bash

child=$1

SOURCE="${child}/tmp"
WRKDIR="${child}/workspace"
OUT="${child}/out"

if [[ -e $SOURCE ]]; then
    rm -Rf $SOURCE
fi

if [[ -e $WRKDIR ]]; then
    rm -Rf $WRKDIR
fi

if [[ -e $OUT ]]; then
    rm -Rf $OUT
fi

mkdir $SOURCE 

cp $child/in/* $SOURCE

mkdir $OUT
