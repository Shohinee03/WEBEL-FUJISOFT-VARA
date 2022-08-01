# Write a python script to calculate product of first N odd natural numbers. Value of N is taken from user.

n=int(input("Enter the upper bound : "))
c=1
product=1
p=0
while(True):
    if(c%2!=0):
        product*=c
        p+=1
    if(p==n):
        break
    c+=1
print("The first ",n," odd natural numbers's product is : ",product)