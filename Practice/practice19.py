#search for a number x in this tuple using loop:

tup = (1,4,9,16,25,36,49,64,81,100,36)
x = int(input("enter a number to search "))
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("found at" , i)
    
    i += 1

