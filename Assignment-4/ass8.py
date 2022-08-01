# prime factor of a given number
def fac(n):
    c=0                     
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
            l.append(i)
    return l
def prime(l):
    l1=[]
    for i in l:
        c=0
        for j in range(2,i):
            if(i%j==0):
                c+=1
        if(c==0):
            l1.append(i)
    return l1    
n=int(input("Enter the number : "))
p=prime(fac(n))
print(p)