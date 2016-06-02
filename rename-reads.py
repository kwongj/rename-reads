#!/usr/bin/env python
# Script by Jason Kwong
# Rename WGS reads eg. for uploading to SRA

# Usage
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Rename reads eg. for uploading to SRA',
	usage='\n  %(prog)s [OPTIONS] KEYFILE')
parser.add_argument('keyfile', metavar='KEYFILE', help='tab-separated file with old names in column 1, new names in column 2')
parser.add_argument('--dir', metavar='READDIR', help='directory to search for reads (not required for MDU reads)')
#parser.add_argument('--fmt', metavar='OUTFMT', default='symlink', help='default=symlink')
parser.add_argument('--version', action='version', version=
	'=====================================\n'
	'%(prog)s v0.1\n'
	'Updated 12-Oct-2015 by Jason Kwong\n'
	'=====================================')
args = parser.parse_args()

import os
import csv
import subprocess
from subprocess import Popen

with open(args.keyfile) as csvfile:
	ids = csv.reader(csvfile, delimiter='\t', quotechar='"')
	for row in ids:
		id1 = row[0]
		id2 = row[1]
		if args.dir:
			proc = subprocess.Popen(['readfinder', '-d', args.dir, id1], stdout=subprocess.PIPE)
			out = proc.communicate()[0].rstrip('\n').split('\t')
		else:
			proc = subprocess.Popen(['mdu-reads', id1], stdout=subprocess.PIPE)
			out = proc.communicate()[0].rstrip('\n').split('\t')
		newR1 = id2 + '_R1.fastq.gz'
		newR2 = id2 + '_R2.fastq.gz'
		print 'ln -s %s %s' % (out[1], newR1)
		print 'ln -s %s %s' % (out[2], newR2)
