#!/bin/bash
DEBUG=1
[[ -n $DEBUG ]] && set -x

function printUsage {
  echo 'Usage: split_video <file_or_dir> [<output_dir>]'
  echo ''
}

function splitFile {
    local fileName=`basename $1`
    ffmpeg -i $1 -qscale:v 2 -vf fps=1 $2/$fileName.%04d.jpg
}

function processDirectory {
    for file in $1/*
    do
        splitFile "$file" $2
    done
}

[[ -z $1 ]] && printUsage && exit 1 

if [[ -f $1 ]] 
then
    echo "$1 - is file" 
    splitFile $1 ${2-.}
fi

if [[ -d $1 ]] 
then
    echo "$1 - is directory"
   processDirectory $1 ${2-.} 
fi

[[ -n $DEBUG ]] && set +x
