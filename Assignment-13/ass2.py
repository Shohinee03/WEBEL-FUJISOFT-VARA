#  Write a python function to calculate sum of squares of first N natural numbers.
def natural(n):
    s=0
    print("The first ",n," natural number's sum is :")
    for i in range(1,n+1):
        s+=i**2
    return s
n=int(input("Enter the number of elements : "))
print(natural(n))