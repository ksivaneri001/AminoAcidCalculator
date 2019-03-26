listU = [["phenylalanine", "phenylalanine", "leucine", "leucine"], ["serine", "serine", "serine", "serine"], ["tyrosine", "tyrosine", "STOP", "STOP"], ["cysteine", "cysteine", "STOP", "tryptophan"]]
listC = [["leucine", "leucine", "leucine", "leucine"], ["proline", "proline", "proline", "proline"], ["histidine", "histidine", "glutamine", "glutamine"], ["arginine", "arginine", "arginine", "arginine"]]
listA = [["isoleucine", "isoleucine", "isoleucine", "methionine"], ["threonine", "threonine", "threonine", "threonine"], ["asparagine", "asparagine", "lysine", "lysine"], ["serine", "serine", "arginine", "arginine"]]
listG = [["valine", "valine", "valine", "valine"], ["alanine", "alanine", "alanine", "alanine"], ["aspartic acid", "aspartic acid", "glutamic acid", "glutamic acid"], ["glycine", "glycine", "glycine", "glycine"]]

listPicker1 = 4
listPicker2 = 4
listPicker3 = 4
stopCheck = "NO STOP"

print("Type in the codon (One base at a time)")
while True:

	row1 = input()
	if row1 == "U":
		listPicker1 = 0
	elif row1 == "C":
		listPicker1 = 1
	elif row1 == "A":
		listPicker1 = 2
	elif row1 == "G":
		listPicker1 = 3
	else:
		print("Error, not an mRNA base")
		break
	# print(listPicker1)

	column = input()
	if column == "U":
		listPicker2 = 0
	elif column == "C":
		listPicker2 = 1
	elif column == "A":
		listPicker2 = 2
	elif column == "G":
		listPicker2 = 3
	else:
		print("Error, not an mRNA base")
		break
	# print(listPicker2)

	row2 = input()
	if row2 == "U":
		listPicker3 = 0
	elif row2 == "C":
		listPicker3 = 1
	elif row2 == "A":
		listPicker3 = 2
	elif row2 == "G":
		listPicker3 = 3
	else:
		print("Error, not an mRNA base")
		break
	# print(listPicker3)

	if listPicker1 == 0:
		stopCheck = listU[listPicker2][listPicker3]
		print(listU[listPicker2][listPicker3])
		if stopCheck == "STOP":
			break
	elif listPicker1 == 1:
		print(listC[listPicker2][listPicker3])
	elif listPicker1 == 2:
		print(listA[listPicker2][listPicker3])
	elif listPicker1 == 3:
		print(listG[listPicker2][listPicker3])