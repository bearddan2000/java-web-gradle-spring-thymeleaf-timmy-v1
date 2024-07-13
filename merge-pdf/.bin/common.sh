#! /bin/bash

function new-one-filter() {
    local folder=$1
    local one=$2
    local filter=`ls $SOURCE | egrep "*${one}*"`

    mkdir -p $folder 
    
    for d in $filter; do
        cp "${SOURCE}/${d}" $folder
    done
}

function new-two-filter() {
    local folder=$1
    local one=$2
    local two=$3
    local filter=`ls $SOURCE | egrep "*${one}*" | egrep "*${two}*"`

    mkdir -p $folder 
    
    for d in $filter; do
        cp "${SOURCE}/${d}" $folder
    done
}

function append-two-filter() {
    local folder=$1
    local one=$2
    local two=$3
    local filter=`ls $SOURCE | egrep "*${one}*" | egrep "*${two}*"`
    
    for d in $filter; do
        cp "${SOURCE}/${d}" $folder
    done
}
function merge(){
    local folder=$1
    local tmp=$2 
    local index=2
    local name=""
    local subfolder=`echo $1 | awk -F'/' '{print $NF}'`

    rm -fR $SOURCE/*

    while  ((`ls $WRKDIR/$subfolder/*.pdf | wc -l` > 150 )); do
        name="timmys-$subfolder-$index.pdf"
        mkdir -p $SOURCE
        mv $(ls $WRKDIR/$subfolder/*.pdf | sort -n | head -n 150) $SOURCE
        pdftk $SOURCE/*.pdf cat output $OUT/$name 2>&1
        rm -fR $SOURCE
        (( index++ ))
    done

    name="timmys-$subfolder.pdf"
    pdftk $WRKDIR/$subfolder/*.pdf cat output $OUT/$name 2>&1

}
