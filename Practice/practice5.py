#WAP to  find the greatest of 3 numbers entered by the user

a = int(input("enter value for A: "))
b = int(input("enter value for B: "))
c = int(input("enter value for C: "))

if (a>b and a>c):
    print (" a is a greater num")
elif(b>c):
    print("b is a greater num")
else:
    print("c is greater num")