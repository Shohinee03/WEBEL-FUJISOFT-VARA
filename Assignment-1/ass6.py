#Area of a triangle
from cmath import sqrt
import math
a=float(input("Enter the length of first side : "))
b=float(input("Enter the length of second side : "))
c=float(input("Enter the length of third side : "))
s=(a+b+c)//2
r=sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is : ",r)