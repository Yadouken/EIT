import sys

if (len(sys.argv) != 3):
    print("Syntaxe : python NERtoOccur.py input output")
    exit()

inputfile = open(sys.argv[1], "r")
line = inputfile.readlines()
outputfile = open(sys.argv[2], "w+")

WordType = {}
WordNB = {}

TotalOccurence = 0
for l in line:
    splittedline = l.split(" ")

    for occurence in splittedline:
        if (occurence == "\n"):
            continue
        data = occurence.split("/")
        TotalOccurence = TotalOccurence + 1

        if data[0] not in WordType:
            WordType[data[0]] = data[1]
            WordNB[data[0]] = 1
        else:
            WordNB[data[0]] = WordNB[data[0]] + 1

""" Affichage des resultats """
for k, v in WordType.items():
    outputfile.write(k + "\t\t" + v + "\t\t" + str(WordNB[k]) + "\t\t" + str(
        ((float(WordNB[k]) / TotalOccurence) * 100)) + "\t\t" + "(" + str(WordNB[k]) + "/" + str(TotalOccurence) + ")\n")
