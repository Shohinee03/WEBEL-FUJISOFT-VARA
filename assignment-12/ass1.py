# Write a python function to print first N natural numbers. 
def natural(n):
    print("The first ",n," natural numbers are :")
    for i in range(1,n+1):
        print(i,end=" ")
n=int(input("Enter the last range : "))
natural(n)
