#LCM of two number
n=int(input("Enter first number : "))
m=int(input("Enter second number : "))
p=max(n,m)
for i in range(p):
    if(p%n==0 and p%m==0):
        print("The LCM is = ",p)    #not complered
    p=p+1
    print(p)
