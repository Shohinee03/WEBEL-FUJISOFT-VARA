#first n even natural numbers in reverse order using range fumction un for loop
n=int(input("Enter the end value of the range : "))
print("The first natural numbers are : ")
for i in range(n,0,-1):
    if(i%2==0):
        print(i)
