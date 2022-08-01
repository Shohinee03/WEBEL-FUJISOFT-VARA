# Write a python script to calculate sum of first N odd natural numbers. Value of N is taken from user.

n=int(input("Enter the upper bound : "))
print("The first ",n," odd natural numbers are : ")
c=1
p=0
while(True):
    if(c%2!=0):
        print(c,end=' ')
        p+=1
    if(p==n):
        break
    c+=1
