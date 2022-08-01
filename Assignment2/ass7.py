# Nature of root of a given quadratic equation
import cmath
a=int(input("Enter the coefficient of x^2 :"))
b=int(input("Enter the coefficient of x :"))
c=int(input("Enter the coefficient of x^0 :"))
d=cmath.sqrt(b**2-4*a*c)
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print("That are the imaginary roots .",r1," ",r2)
