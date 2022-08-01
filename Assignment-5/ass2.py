# Print user choice table.
n=int(input("Enter the table number : "))
print("The table of ",n," is : ")
for i in range(1,11):
    print(n,' * ',i,' = ',n*i)