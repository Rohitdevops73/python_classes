#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#start with an empty dictionary and add one by one. Usee subject name as key and marks as value.

marks ={}

phy = int(input("enter phy marks :"))
marks.update({"phy" : phy})

chem = int(input("enter chem marks :"))
marks.update({"chem" : chem})

maths = int(input("enter maths marks :"))
marks.update({"maths" : maths})


print(marks)