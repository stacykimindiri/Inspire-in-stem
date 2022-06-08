#!/usr/bin/python
#calculation

##########################<ASSIGNMENT1.PY>#########################
#           --AREA OF A CIRCLE
radius = input("Enter radius of a circle")
pi = 3.142
area = pi * int(radius) * int(radius)
print("The area of a circle is " + str(area))

#           --VOLUME OF A CYLINDER
radius = input("Enter radius of the cyclinder")
height = input("Enter height of the cylinder")
pi = 3.142
volume = pi * int(radius) * int(height)
print("The volume of a cylinder is " + str(volume))

#           --SURFACE AREA OF A CYLINDER
base_radius = input("Enter base radius")
height = input("Enter height")
pi = 3.142
surface_area = pi * int(base_radius) * int(height)
print("The surface area of the cyclinde is " + str(surface_area))

#           --VOLUME OF A CUBE
side_length = input("Enter length")
volume = int(side_length) * int(side_length) * int(side_length)
print("The volume of a cube is " + str(volume))


#################################<ASSIGNMENT2.PY>##############################
#squares of numbers to 2 using for loop
numbers = [1,2,3,4,5,6,7,8,9,10]
for numbers in numbers:
    print(numbers**2)

#print a diamond of stars and a pyramid of stars
#pyramid
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1,rows +1 ):
    for space in range(1,(rows-1)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("*",end="")
        k +=1
    k = 0
    print()
#diamond
h = eval(input("Enter diamond's height ; "))
for x in range(h) :
    print("  " * (h - x ) , " * " * (2*x + 1))
for x in range (h - 2 , -1 , -1) :
    print(" " * (h - x) , " * " * (2*x + 1)) 