#!/usr/bin/python

# quick and dirty script to extract a single column of a csv file because 
# sometimes I need just a list.

import csv, argparse

parser=argparse.ArgumentParser()
parser.add_argument('infile', help="input file")
parser.add_argument('col',help="column name")
parser.add_argument('-o','--outfile', help="output file")
parser.add_argument('-B','--prefix', help="add text before", default="")
parser.add_argument('-A','--postfix',help="add text after", default="")
args=parser.parse_args()

infile=args.infile
outfile=args.outfile
col=args.col
list = []

with open(infile,'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        list.append('{0}{1}{2}'.format(args.prefix,row[col],args.postfix))
if outfile:
    with open(outfile,'w') as textfile:
        textfile.write('\n'.join(list))
else:
    print(*list)