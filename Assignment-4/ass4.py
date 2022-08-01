#all prime numbers in a given range
n=int(input("Enter the range : Start value :"))
m=int(input("End value : "))
print("The prime numbers are ")
for j in range (n,m+1):
    c=0
    for i in range(1,j):
        if(j%i==0):
            c+=1
    if(c==1):
        print(j)