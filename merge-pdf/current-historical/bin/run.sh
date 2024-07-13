#! /bin/bash

parent=$1

child=$2

prev=$3

# rename 'crdowload' files to pdf
find $child -type f -name "*crdownload" -execdir  sh -c 'x={}; mv "$x" $(echo $x | sed 's/\.crdownload//g')' \; 2> /dev/null

# create a directory for pdf
# put all pdf in new directory
mkdir -p $child/in

# move data
mv $child/*.pdf $child/in 2> /dev/null

$PWD/$prev/bin/p-sort.sh $parent $child $prev
