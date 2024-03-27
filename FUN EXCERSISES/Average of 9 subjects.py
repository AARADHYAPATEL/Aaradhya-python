eng = int(input("Enter the marks for English: "))
sci = int(input("Enter the marks for science: "))
ssc = int(input("Enter the marks for Social science: "))
lang = int(input("Enter the marks for language: "))
comp = int(input("Enter the marks for computers: "))
math = int(input("Enter the marks for mathematics: "))
bio = int(input("Enter the marks for biolagy:  "))
phy = int(input("Enter the marks for physics: "))
chem = int(input("Enter the marks for chemistry: "))
total = eng + sci + ssc + lang + comp + math + bio + phy + chem
print("Total marks for 9 subjects: ", total)
average = total / 9
print("Average of 9 subjects: ", average)