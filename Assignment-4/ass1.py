#prime or not
n=int(input("Enter the number : "))
c=0
for i in range(2,n):
    if(n%i==0):
        c+=1
if(c==0):
    print("The number is prime .")
else:
    print("The number is composite .")
