#search for anumber x in the tuple using loop:

#this is a linear search

num = [ 1,4,9,16,25,36,49,64,81,100]
x = int(input ("enter a num to search from num : "))

idx = 0
for el in num:
    if (el == x):
        print("the num found at index", idx)
        break
    idx += 1
    