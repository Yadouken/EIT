import sys

if (len(sys.argv) != 3):
	print("Syntaxe : python LimaToText.py tonTxt.conll resultat.txt")
	exit()
"""
python LimaToText.py TP1_TAL\wsj_0010_sample.txt.conll Text.txt
"""
file = open(sys.argv[1],"r")
Xfile = open(sys.argv[2],"w")

"""
Liste des etiquettes LIMA a remplacer par les etiquettes PTB
"""
listeLIMA = ["SCONJ","SENT","COMMA","COLON"]
listePTB = ["CC",".",",",":"]

lignes = file.readlines()
for i in range(len(lignes)):
	lignes[i] = lignes[i].split('\t')

for i in range(len(lignes)):
	find = False
	if len(lignes[i]) >= 4:
		mots = lignes[i][1].split(' ')
		if (len(mots) == 1):
			for j in range(0,len(listeLIMA)):
				if (listeLIMA[j] == lignes[i][4]):
					Xfile.write(mots[0]+"_"+listePTB[j]+" ")
					find = True
					break
			if (find == False):
				Xfile.write(mots[0]+"_"+lignes[i][4]+" ")
		elif (len(mots) > 1):
			resStr = ""
			for j in range(0,len(mots)):
				resStr = resStr + mots[j]
				if (j < len(mots)-1):
					resStr = resStr + " "
			for j in range(0,len(listeLIMA)):
				if (listeLIMA[j] == lignes[i][4]):
					Xfile.write(mots[0]+"_"+listePTB[j]+" ")
					find = True
					break
			if (find == False):
				Xfile.write(resStr+"_"+lignes[i][4]+" ")