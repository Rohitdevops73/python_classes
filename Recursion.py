#recursive function

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)



#to calculate factorial of n

def fact(n):
    if (n == 0 or n ==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))
#wriete program to pring the fibonacci series

def fib (n):
    if (n == 0 ):
        return 0
    elif (n == 1):
        return n
    else:
        return fib(n-1)+ fib(n-2)

