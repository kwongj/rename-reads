#!/bin/sh
# Script by JK
# Puts read files into folders.
# Type 'run-put_into_folders.sh -h' for help.

#..............................................................................

# Functions

function msg 
{
  echo -e "$*"
}

function err 
{
  echo "ERROR: $*" 1>&2
  exit 1
}

function usage 
{
  msg "Name:\n  run-put_into_folders"
  msg "Author:\n  Jason Kwong <j.kwong1@student.unimelb.edu.au>"
  msg "Description:\n  Puts read files into folders" 
  msg "Usage:\n  run-put_into_folders.sh <readsA_R1.fastq.gz> <readsA_R2.fastq.gz ... <readsN_R2.fastq.gz>"
  msg "Parameters:"
  msg "  <reads.fastq.gz>	Reads to place into folders. Should be renamed with underscore after unique desired name"
  msg "Options:"
  msg "  -h             Show this help"
  exit 0 
}

#..............................................................................

# Options
while getopts "h" opt; do
    case $opt in
        h)
            usage ;;
    esac
done

# skip over options to pass arguments
shift $((OPTIND - 1))

# read our mandatory positional parameters
[[ $# -lt 1 ]] && usage

#..............................................................................

for f in "$@" ; do
	d=${f##*/}
	fname=${d%%_*}
	printf "%s\n" "mkdir -pv $fname"
	printf "%s\n" "mv -v $f $fname/"
done

