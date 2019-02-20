import numpy as np
import sys

if (len(sys.argv) != 3):
	print("Syntaxe : python EXO3.py tonTxt.conll resultat.txt")
"""TP1_TAL/wsj_0010_sample.txt.conll"""
file = open(sys.argv[1],"r")
Xfile = open(sys.argv[2],"w")

lignes = file.readlines()
for i in range(len(lignes)):
	lignes[i] = lignes[i].split('\t')

for i in range(len(lignes)):
	if len(lignes[i]) >= 4:
		mots = lignes[i][1].split(' ')
		if (len(mots) == 1):
			Xfile.write(mots[0]+"_"+lignes[i][4]+" ")
		elif (len(mots) > 1):
			resStr = ""
			for j in range(0,len(mots)):
				resStr = resStr + mots[j]
				if (j < len(mots)-1):
					resStr = resStr + " "
			Xfile.write(resStr+"_"+lignes[i][4]+" ")