# Anything commented out was used only for testing the code

# Lists representing the codon chart
listU = [["phenylalanine", "phenylalanine", "leucine", "leucine"], ["serine", "serine", "serine", "serine"], ["tyrosine", "tyrosine", "STOP", "STOP"], ["cysteine", "cysteine", "STOP", "tryptophan"]]
listC = [["leucine", "leucine", "leucine", "leucine"], ["proline", "proline", "proline", "proline"], ["histidine", "histidine", "glutamine", "glutamine"], ["arginine", "arginine", "arginine", "arginine"]]
listA = [["isoleucine", "isoleucine", "isoleucine", "methionine"], ["threonine", "threonine", "threonine", "threonine"], ["asparagine", "asparagine", "lysine", "lysine"], ["serine", "serine", "arginine", "arginine"]]
listG = [["valine", "valine", "valine", "valine"], ["alanine", "alanine", "alanine", "alanine"], ["aspartic acid", "aspartic acid", "glutamic acid", "glutamic acid"], ["glycine", "glycine", "glycine", "glycine"]]

# List where bases will be added
bases = []

# Varibles that determine the list and the element in the list chosen; set to 4 as a default value
listPicker1 = 4
listPicker2 = 4
listPicker3 = 4

# Variable that breaks the loop when a STOP codon is hit; set to 'NO STOP' as a default value
stopCheck = "NO STOP"

# Function that takes each codon and gives the amino acid for each one is defined here
def oneByOne():

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
      print("Not an mRNA base")
      break
  #	print(listPicker1)

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
      print("Not an mRNA base")
      break
  #	print(listPicker2)

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
      print("Not an mRNA base")
      break
  #	print(listPicker3)

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

# Function that takes all the bases first and gives the amino acids second is defined here
def allAtOnce():

  print("Type in each base one at a time. Hit enter without typing when you are done.")
  print('')
  print("Note: If the number of bases typed is less than 3, an error will occur. When this happens, run the code again. If the number of bases typed is greater than 3 but is not a multiple of 3, then the error can be ignored. It simply means that the last bases in the mRNA did not make up a codon.")
  x = 0

  while True:

    newBase = input()
    if newBase == "U" or newBase == "C" or newBase == "A" or newBase == "G":
      bases.append(newBase)
      # print(bases)
    elif newBase == '':
      while x < len(bases):

        if bases[x] == "U":
          listPicker1 = 0
        elif bases[x] == "C":
          listPicker1 = 1
        elif bases[x] == "A":
          listPicker1 = 2
        elif bases[x] == "G":
          listPicker1 = 3
        # print(listPicker1)

        if bases[x + 1] == "U":
          listPicker2 = 0
        elif bases[x + 1] == "C":
          listPicker2 = 1
        elif bases[x + 1] == "A":
          listPicker2 = 2
        elif bases[x + 1] == "G":
          listPicker2 = 3
        # print(listPicker1)

        if bases[x + 2] == "U":
          listPicker3 = 0
        elif bases[x + 2] == "C":
          listPicker3 = 1
        elif bases[x + 2] == "A":
          listPicker3 = 2
        elif bases[x + 2] == "G":
          listPicker3 = 3
        # print(listPicker1)

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

        x = x + 3

      break

    else:
      print("Not an mRNA base")
      break

    
# Allows user to choose which function to run
print("Would you like to type the bases one codon at a time (1), or would you like to type the bases in a row (2)?")
option = 0
option = input()
if option == "1":
  oneByOne()
elif option == "2":
  allAtOnce()
else:
  print("You may only type 1 or 2")
