#print first n prime number
from itertools import count


n=int(input("Enter the last range : "))
print("The prime numbers are ")
for j in range (1,n+1):
    c=0
    for i in range(1,j):
        if(j%i==0):
            c+=1
    if(c==1):
        print(j)