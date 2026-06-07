#WAF to find the factorial of n .(n is the parameter)

n = int(input("enter the number : "))

def cal_factorial(n):
    fac =1
    for ele in range(1,n+1):
        fac *= ele
    print(fac)

cal_factorial (n)