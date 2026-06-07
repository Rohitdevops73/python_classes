#WAF to input a number n and retun odd if the number is oDD and even if the number is even

n = int(input("enter a number: "))

def odd_even(n):
    if (n%2 != 0):
        print("odd")
    else:
        print("even")

odd_even(n)
