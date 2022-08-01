#print first n odd natural numbers in reverse order using for loop.
n=int(input("Enter the end value of the range : "))
print("The first natural numbers are : ")
for i in range(n,0,-1):
    if(i%2==1):
        print(i)
