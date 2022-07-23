m=int(input('Enter the month in numeric form :'))
yr=int(input('Enter the year :'))
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
	print('Number of dayes of this month is : 31')
elif(m==2 and (yr%400==0 or (yr%4==0) and yr%100!=0)):
	print('Number of day in this month is : 29')
elif(m==2):
	print('Number of days in this month is : 28')
else:
	print('Number of days in this month is : 30')
