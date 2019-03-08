##########################################################################
#
#	This script converts LIMA labels into universal labels
#
##########################################################################

import sys

if (len(sys.argv) != 4):
	print("Syntaxe : python PTBToUniversal.py dicoPTBtoUNIV textEtiqLIMA resultat.txt")
	exit()

tags = open(sys.argv[1], "r")
tagline = tags.readlines()

# Filling the conversion dictionary
dico = { }
for i in range(len(tagline)):
	tagline[i] = tagline[i].split(' ')
	dico[tagline[i][0]] = tagline[i][1].rstrip()

file = open(sys.argv[2],"r")
output = open(sys.argv[3], "w")
line = file.read()
line = line.split('_')

output.write(line[0])
for i in range(1, len(line)):
	if line[i].split(' ')[0] in dico.keys():
		line[i] = str.replace(line[i], line[i].split(' ')[0], dico[line[i].split(' ')[0]])
	output.write('_' + line[i])
