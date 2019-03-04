import sys

if (len(sys.argv) != 3):
    print("Syntaxe : python script.py input output")
    exit()

inputfile = open(sys.argv[1], "r")
line = inputfile.readlines()
outputfile = open(sys.argv[2], "w+")

for l in line:
    splittedline = l.split(" ")

    for occurence in splittedline: 
        if (occurence == "\n"):
            continue
        data = occurence.split("/")

        if(len(data) > 1):
            if(data[1] == "PERSON" or data[1] == "LOCATION" or data[1] == "ORGANIZATION"):
                outputfile.write(data[0] + "_NOUN ")
            else:
                outputfile.write(data[0] + " ")
        else:
            outputfile.write(data[0] + " ")
    outputfile.write("\n")
