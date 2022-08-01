# Write a python script to calculate sum of first N natural numbers. Value of N is taken from user.

n=int(input("Enter the upper bound : "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first ",n,' natural number is : ',sum)