#HCF of two number
n=int(input("Enter the first number : "))
m=int(input("enter thr second number : "))
hcf=0
for i in range(1,m):
    if(n%i==0 and m%i==0):
        hcf=i
print("The hight-co-factor of the two number is : ",hcf)