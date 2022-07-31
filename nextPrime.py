n=int(input("Enter the number : "))
p=n+1
for i in range(2,p):
    if(p%i==0):
        p+=1
else:
    print("The next prime number is : ",p)