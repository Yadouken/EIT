import numpy as np

file = open("wsj_0010_sample.txt.conll","r")
Xfile = open("ABABABA.txt","w")

lignes = file.readlines()
for i in range(len(lignes)):
	lignes[i] = lignes[i].split('\t')

for i in range(len(lignes)):
	#print(len(lignes[i]))
	if len(lignes[i]) >= 4:
		mots = lignes[i][1].split(' ')
		for mot in mots:
			Xfile.write(mot+"_"+lignes[i][4]+" ")