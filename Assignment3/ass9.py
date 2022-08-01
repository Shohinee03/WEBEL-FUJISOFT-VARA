# Write a python script to calculate factorial of a number Number is taken from user.

def fac(n):
    if(n==1):
        return n
    else:
        return n * fac(n-1)
n=int(input("Enter the number : "))
print("The factorial of ",n,"is = ",fac(n))

