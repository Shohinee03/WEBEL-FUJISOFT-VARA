# Take user input 10 subjects marks and show pass or fail and division also
l=[]
print("Enter 5 subject numbers one by one : ")
for i in range(1,6):
    l.append(int(input()))
c=0
for i in l:
    if(i<30):
        c+=1
if(c>0):
    print("The student is not passd .")
else:
    p=sum(l)//5
    print("The student is passed with ",p,'% number')
    if(p>90):
        print('O')
    elif(p>80 and p<=90):
        print('E')
    elif(p>70 and p<=80):
        print('A+')
    elif(p>60 and p<=70):
        print('A')
    elif(p>50 and p<=60):
        print('B+')
    elif(p>40 and p<=50):
        print('B')
    elif(p>30 and p<=40):
        print('C')
    else:
        print("Not passed")
