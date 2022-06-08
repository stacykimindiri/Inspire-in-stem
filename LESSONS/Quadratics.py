#!/usr/bin/python
#           Quadratic equations
#        Name : Stacy Emmy
#        Date : 31 / 5 / 20.
# Create a function to find the roots of a guadratic equation
import math
a=int(input("Enter the co-efficient of the first term"))
b=int(input("Enter the co-efficient of the second term"))
c=int(input("Enter the constant"))
def find_roots(a,b,c):
    y1=(-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
    y2=(+b - math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("The roots of the quadratic equation are:",y1,y2)
find_roots(a,b,c)
################################################################
import math
a=int(input("Enter the co-efficient of the first term"))
b=int(input("Enter the co-efficient of the second term"))
c=int(input("Enter the constant"))
w = math.sqrt((b**2)-(4*a*c))
def find_roots(a,b,c):
    y1=(-b  + w) / (2*a)
    y2=(-b  - w) / (2*a)
    print("The roots of the quadratic equation are:",y1,y2)
find_roots(a,b,c)

    
