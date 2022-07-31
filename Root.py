import cmath
a=eval(input('Enter the coeficient of x^2 : '))
b=eval(input('Enter the coeficient of x : '))
c=eval(input('Enter the coeficient of x^0 : '))
d=b**2-(4*a*c)
r=cmath.sqrt(d)
print(r)
if(d>0):
	s=(-b+r)/(2*a)
	t=(-b-r)/(2*a)
elif(d==0):
	t=s=-b/2*a
else:
	s=eval((-b+r)/2*a)
	t=eval((-b-r)/2*a)
print('The roots are : ',s,' ',t)

