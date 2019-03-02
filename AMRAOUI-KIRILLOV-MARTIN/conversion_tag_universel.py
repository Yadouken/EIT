import sys

if (len(sys.argv) != 4):
	print("Syntaxe : python conversion_tag_universel.py dicoPTBtoUNIV textEtiqLIMA resultat.txt")
	exit()

tags = open(sys.argv[1], "r")
tagline = tags.readlines()
dico = { }
#print(file.read())
for i in range(len(tagline)):
	tagline[i] = tagline[i].split(' ')
	dico[tagline[i][0]] = tagline[i][1].rstrip()

file = open(sys.argv[2],"r")

output = open(sys.argv[3], "w")

line = file.readlines()

line[0] = line[0].split('_')
output.write(line[0][0])
for i in range(1, len(line[0])):
	#print(line[0][i].split(' ')[0])
	if line[0][i].split(' ')[0] in dico.keys():
		line[0][i] = str.replace(line[0][i], line[0][i].split(' ')[0], dico[line[0][i].split(' ')[0]])
		output.write('_' + line[0][i])
	#splitted = line[0][i].split('_')
	#print(splitted[1])
	#str.replace(splitted[1], splitted[1], dico[splitted[1]])
