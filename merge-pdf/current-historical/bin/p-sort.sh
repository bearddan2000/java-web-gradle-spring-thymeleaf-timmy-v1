#! /bin/bash
parent=$1

child=$2

prev=$3

source $PWD/.bin/constants.sh $child

pdftk $SOURCE/*.pdf cat output $OUT/timmy.pdf

cp $OUT/* $parent