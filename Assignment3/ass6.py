# Write a python script to print first N natural numbers in reverse order. Value of N is taken from user.

n=int(input("Enter the upper bound : "))
for i in range(n,0,-1):
    print(i,end=' ')