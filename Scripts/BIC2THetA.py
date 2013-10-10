#! /usr/bin/python
# programmer: bchen4
# Usage: BIC2ThetA.py input.bicseg > output.theta
# Usage: convert bicseg file to theta input(interval_count_file)

import sys
import string


def main():
	try:
		bic = open(sys.argv[1],"r")
	except IOError,message:
		print >>sys.stderr, "Can not open input file.",message
		sys.exit(0)
	
	print "ID\tchrm\tstart\tend\ttumorCount\tnormalCount"
	for item in bic:
		buf = item.rstrip().split("\t")
		if buf[0]!= "chrom":
			chr = buf[0].replace("chr","")
			id = "start_"+chr+"_"+buf[1]+":end_"+chr+"_"+buf[2]
			print "\t".join([id,chr,buf[1],buf[2],buf[3],buf[4]])


if __name__=="__main__":
	main()
