year=int(input("Enter the year : "))
if(year%400==0):
    print("The year is leap year .")
elif(year%100==0):
    print("The year is not leap year .")
elif(year%4==0):
    print("The year is leap year .")
else:
    print("The year is not leap year .")