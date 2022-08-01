# Take input from the user and show the greatest part betwen real and imaginary part.
import cmath
from numpy import imag, real
n=complex(input("Enter the complex number : "))
print(max(n.real,n.imag))