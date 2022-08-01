# All armstrong numbers under 1000
print("The Armstrong numbers under 1000 are : ")
for i in range(1000):
    rev=0
    temp=i
    while(i>0):
        rim=i%10
        rev+=rim**3
        i//=10
    if(temp==rev):
        print(rev)

