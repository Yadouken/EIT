import re

def extractType(tags):
	result = []
	for i in range(len(tags)):
		result.append(str.replace(re.search("\"[A-Z]+\"", tags[i]).group(0), "\"", ""))
	return result

if __name__ == "__main__":
	f = open("formal-tst.NE.key.04oct95_small.ne", "r")
	output = open("formal-tst.NE.key.04oct95_small.withtags.ne", "w")
	text = f.readlines()
	
	for i in range(len(text)):
		status = re.search(' STATUS="[A-Z]+"', text[i])
		if status != None:
			text[i] = str.replace(text[i], status.group(0), "")
			print("###############################")
			print(text[i])
			print("###############################")	
			print(status.group(0))

		print(text[i])	
		typ = re.findall('<[A-Z]+ TYPE="[A-Z]+"', text[i])

		if typ != None:
			realTyp = extractType(typ)

		result = re.findall('<[A-Z]+ TYPE="[A-Z]+">([^<]+)</[A-Z]+>', text[i])

		for j in range(len(realTyp)):
			tag = re.search('<[A-Z]+ TYPE="[A-Z]+">([^<]+)</[A-Z]+>', text[i])
			if tag != None:
				#Replace realTyp[j] by "NOUN" in next line to get Universal tags
				if ((realTyp[j] == "PERSON") or (realTyp[j] == "ORGANIZATION") or (realTyp[j] == "LOCATION")):
					text[i] = str.replace(text[i], tag.group(0), result[j] + "_" + realTyp[j])
				else:
					text[i] = str.replace(text[i], tag.group(0), result[j])
		output.write(text[i])