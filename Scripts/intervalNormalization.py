#!/usr/bin/python
# programmer : bbc
# usage:

import sys
import re
import random
import string
import pandas as pd

def main():
	try:
		infile = pd.read_table(sys.argv[1])
	except IOError,message:
		print >> sys.stderr, "cannot open file",message
		sys.exit(1)
	
	tumor_sum = sum(infile['tumorCount'])
	normal_sum = sum(infile['normalCount'])
	print "# tumor_total_count",tumor_sum, "normal_total_count",normal_sum
	print '\t'.join(infile.columns) # print header
	
	for row in infile.values:
		interval_len = float(int(row[3])- int(row[2]))
		row[4] = str((int(row[4])/ interval_len) * (1000000000/tumor_sum))
		row[5] = str((int(row[5])/ interval_len) * (1000000000/normal_sum))
		row[1] = str(row[1])
		row[2] = str(row[2])
		row[3] = str(row[3])
		print '\t'.join(row)
if __name__=="__main__":
	main()
