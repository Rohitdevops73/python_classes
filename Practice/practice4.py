#WAP to check if a number entered by the user is odd or even

num = int(input("enter a number :"))

if (num % 2 ==0):
    result= "This is a EVEN"
else:
    result= "this is ODD"
print(result)