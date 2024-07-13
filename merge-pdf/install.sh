#! /bin/bash

function start-up(){
    rm -fR out/*

    for d in `find $pwd -type d -name "bin"`; do

        local prev=`echo $d | sed -e 's/\/bin//g' `

        local clean=`echo $prev | sed -e 's/\.\///g'`

        sudo chown -R oem:oem $d

        sudo chmod -R +x $d

        rm -f $d/*.sh

        cp .bin/*run.sh $d

        cp $prev/*.sh $d

        sudo chmod -R +x $d

        $d/run.sh $PWD/out $PWD/$clean/bin $clean

    done
}

function tear-down() {
    for d in `find $pwd -type d -name "bin"`; do

        rm -Rf $d

        mkdir -p $d

    done
}

while getopts ":ud" opts; do
  case $opts in
    u)
      start-up ;;
    d)
      tear-down ;;
  esac
done