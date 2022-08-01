# Take month value in numeric form and show days in it.
year=int(input("Enter the year : "))
m=int(input("Enter the month value in numeric form : " ))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==10:
    print("There is 31 days in this month.")
elif(m==2 and (year%400!=0 and year%100==0)or year%4!=0):
    print("This year is not leap year .So number of month is 28")
elif(m==2 and (year%400==0)or year%4==0):
    print("Number of month is 29:")
else:
    print("There is 30 days in this month.")
