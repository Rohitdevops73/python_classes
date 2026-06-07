#WAP to find the factorial of first n numbers. (using for)

# n = int(input("enter the number n: "))

# fac = 1
# for i in range (1, n+1):
#     fac *= i # fac = fac*i
    
# print("the factorial for n is : ",fac)


#using while

n = int(input("enter the number n: "))

fac =1 
i =1
while i <= n:
    fac *= i
    i += 1
print ("the fac value is : ", fac)