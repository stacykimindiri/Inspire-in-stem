#!/usr/bin/python
#####################################################
#      for loops with lists
#       Name : Stacy Emmy
#       Date : 24 / 5 / 20.
#####################################################
squares = []
for number in range(0,10):
    square = number**2
    squares.append(square)
print(squares)

cubes = []
for number in range(0,10):
    cube = number**3
    cubes.append(cube)
print(cubes)
#sum for numbers between 1 and 100
sum = 0
for number in range(0,100):
    sum = sum + number
print(sum)

#if statements
age = 24
if age >= 18:
    print("you are allowed to drive")
else:
    print("you are too young to drive")

