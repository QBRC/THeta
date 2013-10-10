#! /usr/bin/python
# programmer: bchen4
# Usage:makeBICSEQconfigFile.py tumorSeqDIR/ normalSeqDIR/

import sys
import string
from os import listdir
from os.path import isfile,join


def main():
	try:
		case_path = str(sys.argv[1])
		control_path = str(sys.argv[2])
	except:
		print >>sys.stderr, "Usage:makeBICSEQconfigFile.py caseDIR/ controlDIR/ \nInput error. Please check the path."
	caseFile = [f for f in listdir(case_path) if isfile(join(case_path,f))]
	controlFile = [f for f in listdir(control_path) if isfile(join(control_path,f))]
	#print caseFile
	#print controlFile
	try:
		output = open(str(sys.argv[3])+".BICconfig","w")
		outerr = open(str(sys.argv[3])+".err","w")
	except:
		output = open("testBIC.config","w")
		outerr = open("testBIC.err","w")

	print >> output, "chrom\tcase\tcontrol"
	print >> outerr, "Files cannot be found in control directory:"
	for i in caseFile:
		if controlFile.count(i)>0:
			chr = i.split(".")[0]
			case = case_path+i
			control = control_path+i
			print >>output, "%s\t%s\t%s" % (chr,case,control)
		else:
			print >>outerr,i


if __name__=="__main__":
	main()
