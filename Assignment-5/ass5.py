# a,b=map(int,input("Enter upper bound and lower bound seperated by space : ").split())

# Printing a sequence of numbers un user given range and step.
a=int(input("Enter the upper bound : "))
b=int(input("Enter the lower bound : "))
s=int(input("Enter the step value : "))
for i in range(a,b+1,s):
    print(i,end=' ')
