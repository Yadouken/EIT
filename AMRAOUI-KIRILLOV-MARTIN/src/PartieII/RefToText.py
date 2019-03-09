##########################################################################
#
#	This script converts reference table into reference text
#
##########################################################################

import sys

if __name__ == "__main__":
	if (len(sys.argv) != 3):
		print("Syntaxe : python RefToText.py referenceFile resultFile")
		exit()

	f = open(sys.argv[1], "r")
	output = open(sys.argv[2], "w")

	lines = f.readlines()

	for i in range(len(lines)):
		res = str.split(lines[i], '\t')
		res[1] = str.replace(res[1], '\n', ' ')
		output.write(res[0] + "_" + res[1])