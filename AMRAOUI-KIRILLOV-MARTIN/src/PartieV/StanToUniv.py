import sys

if (len(sys.argv) != 3):
	print("Syntaxe : python StanToUniv.py tonTxtStan resUniv.txt")
	exit()

file = open(sys.argv[1],"r")
Xfile = open(sys.argv[2],"w")

lignes = file.readlines()



ponctuation = [",",".","(",")",";","TimESPACEWirth"]
for i in range(len(lignes)):
    lignes[i] = str.replace(lignes[i], "\'s", '' )
    lignes[i] = str.replace(lignes[i], "-LRB-/O ", '(' )
    lignes[i] = str.replace(lignes[i], "-RRB-", ')' )
    lignes[i] = str.replace(lignes[i], "-", '/O ' )
    lignes[i] = lignes[i].split(' ')
for i in range(len(lignes)):
    for j in range (0,len(lignes[i])):
        sautDeLigne = False
        paire = lignes[i][j].split('/')
        if (paire[0] == "." and j != (len(lignes[i]) - 1) and lignes[i][j+1].split('/')[0] not in ponctuation):
            paire[0] = str.replace(paire[0], ".", ".\n" )
            sautDeLigne = True
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
            if (nextPaire[0] != "." and nextPaire[0] != "," and nextPaire[0] != ")" and sautDeLigne == False):
                Xfile.write(" ")
