import sys

if (len(sys.argv) != 3):
	print("Syntaxe : python StanToUniv.py tonTxtStan resUniv.txt")
	exit()

file = open(sys.argv[1],"r")
Xfile = open(sys.argv[2],"w")

lignes = file.readlines()

for i in range(len(lignes)):
	lignes[i] = lignes[i].split(' ')
for i in range(len(lignes)):
    for j in range (0,len(lignes[i])):
        paire = lignes[i][j].split('/')
        if (len(paire) != 2):
        	continue
        if (paire[1] == "PERSON" or paire[1] == "ORGANIZATION" or paire[1] == "LOCATION"):
            Xfile.write(paire[0] + "_NOUN")
        else:
            Xfile.write(paire[0])
        if (j != len(lignes[i]) - 1):
            nextPaire = lignes[i][j+1].split('/')
            if (len(paire) != 2):
                continue
            if (nextPaire[0] != "." and nextPaire[0] != "," ):
                Xfile.write(" ")
        