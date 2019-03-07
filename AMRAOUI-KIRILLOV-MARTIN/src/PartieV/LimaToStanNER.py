import sys

if (len(sys.argv) != 3):
	print("Syntaxe : python LimaToStanNER.py tonTxt.lima resultat.txt")
	exit()
"""
python LimaToText.py TP1_TAL\wsj_0010_sample.txt.conll Text.txt
"""
file = open(sys.argv[1],"r")
Xfile = open(sys.argv[2],"w")

lignes = file.readlines()
for i in range(len(lignes)):
	lignes[i] = lignes[i].split('\t')
for i in range(len(lignes)):
	if len(lignes[i]) >= 4:
		if (lignes[i][5] == "Person.PERSON"):
			groupMots = lignes[i][1].split(' ')
			for j in range (0,len(groupMots)):
				if (j != len(groupMots) - 1):
					Xfile.write(groupMots[j]+"ESPACE")
				else:
					Xfile.write(groupMots[j]+"/PERSON ")
		elif (lignes[i][5] == "Organization.ORGANIZATION"):
			groupMots = lignes[i][1].split(' ')
			for j in range (0,len(groupMots)):
				if (j != len(groupMots) - 1):
					Xfile.write(groupMots[j]+"ESPACE")
				else:
					Xfile.write(groupMots[j]+"/ORGANIZATION ")
		elif (lignes[i][5] == "Location.LOCATION"):
			groupMots = lignes[i][1].split(' ')
			for j in range (0,len(groupMots)):
				if (j != len(groupMots) - 1):
					Xfile.write(groupMots[j]+"ESPACE")
				else:
					Xfile.write(groupMots[j]+"/LOCATION ")
		else:
			groupMots = lignes[i][1].split(' ')
			for j in range (0,len(groupMots)):
				Xfile.write(groupMots[j]+"/O ")