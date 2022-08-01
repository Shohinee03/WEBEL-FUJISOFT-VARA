# Write a python script to print first N natural numbers. Value of N is taken from user.

n=int(input("Enter the upper bound : "))
for i in range(1,n+1):
    print(i,end=' ')
