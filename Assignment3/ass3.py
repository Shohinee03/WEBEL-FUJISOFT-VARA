# Write a python script to print first 10 odd natural numbers.

print("The first 10 odd natural numbers are : ")
c=1
p=0
while(True):
    if(c%2!=0):
        print(c,end=' ')
        p+=1
    if(p==10):
        break
    c+=1
