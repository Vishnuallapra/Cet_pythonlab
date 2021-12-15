num=int(input("Enter a number:"))
def fact(num):
    n=num
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact
print("Factorial of ",num,"is",fact(num)) 