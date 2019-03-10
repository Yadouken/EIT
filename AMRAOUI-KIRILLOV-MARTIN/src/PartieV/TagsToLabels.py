##########################################################################
#
#	This script converts an input text written with reference tags into
#	a text written with labels (tag detection is made using regular 
#	expressions. You can configure line 48 to either get a text with 
#	universal tags or Stanford tags.
#
##########################################################################

import re
import sys

# Returns the named entity attached to the tag given
def extractType(tags):
	result = []
	for i in range(len(tags)):
		result.append(str.replace(re.search("\"[A-Z]+\"", tags[i]).group(0), "\"", ""))
	return result

if __name__ == "__main__":
	if (len(sys.argv) != 3):
		print("Syntaxe : python TagsToLabels.py referenceFile resultFile")
		exit()

	f = open(sys.argv[1], "r")
	output = open(sys.argv[2], "w")
	text = f.readlines()
	
	for i in range(len(text)):
		text[i] = str.replace(text[i], '\'s', '')
		text[i] = str.replace(text[i], '\n', ' ')
		if (len(text[i]) == 1 and text[i][0] == ' ' ):
			text[i] = str.replace(text[i], ' ', '')

		# Removal of unnecessary flags
		status = re.search(' STATUS="[A-Z]+"', text[i])
		if status != None:
			text[i] = str.replace(text[i], status.group(0), "")

		# Extraction of TYPE value
		typ = re.findall('<[A-Z]+ TYPE="[A-Z]+"', text[i])
		if typ != None:
			realTyp = extractType(typ)

		# Conversion from reference tags to [universal] labels
		result = re.findall('<[A-Z]+ TYPE="[A-Z]+">([^<]+)</[A-Z]+>', text[i])
		for j in range(len(realTyp)):
			tag = re.search('<[A-Z]+ TYPE="[A-Z]+">([^<]+)</[A-Z]+>', text[i])
			if tag != None:
				# In this project we only consider three named entities, the others are just taken off
				if ((realTyp[j] == "PERSON") or (realTyp[j] == "ORGANIZATION") or (realTyp[j] == "LOCATION")):
					# Replace realTyp[j] by "NOUN" in next line to get Universal tags
					if (len(result[j]) > 1):
						result[j] = str.replace(result[j], " ","ESPACE")
					text[i] = str.replace(text[i], tag.group(0), result[j] + "_" + "NOUN")
				else:
					text[i] = str.replace(text[i], tag.group(0), result[j])
		
		output.write(text[i])
