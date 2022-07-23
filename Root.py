import math
a=eval(input('Enter the coeficient of x^2 : '))
b=eval(input('Enter the coeficient of x : '))
c=eval(input('Enter the coeficient of x^0 : '))
d=b**2-(4*a*c)
r=eval(math.sqrt(d))
if(d>0):
	s=(-b+r)/4*a*c
	t=(-b-r)/4*a*c
elif(d==0):
	t=s=-b/4*a*c
else:
	s=eval((-b+r)/4*a*c)
	t=eval((-b-r)/4*a*c)
print('The roots are : ',s,' ',t)

