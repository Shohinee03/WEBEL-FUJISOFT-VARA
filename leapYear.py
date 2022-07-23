n=int(input('Enter the year : '))
if(n%400==0):
	print('It is leap year.')
elif(n%100==0):
	print('It is not leap year .')
elif(n%4==0):
	print('It is leap year .')
else:
	print('It is not leap year .')