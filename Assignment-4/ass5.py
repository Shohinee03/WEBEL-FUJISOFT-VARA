#Two numbers are co-prime or not
from re import I


n=int(input("Enter first number : "))
m=int(input("Enter second number : "))
hcf=0
for i in range(1,n+1):
    if(n%i==0 and m%i==0):
        hcf=i
if (hcf==1):
    print("The number are co-prime . ")
else:
    print("The number are not co-prime . ")