# Find greatest among three numbers.
a,b,c=map(int,input("Enter three numbers :").split())
if(a>b):
    t=a
else:
    t=b
if (t>c):
    r=t
else:
    r=c
print("The greatest among the given numbers is : ",r)

# other way
'''a,b,c=map(int,input("Enter three numbers :").split())
if(a>b and a>c):
    print(a," i the greatest number .")
elif(b>a and b>c):
    print(b," i the greatest number .")
else:
    print(c," i the greatest number .")'''