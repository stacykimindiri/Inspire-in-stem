#!/usr/bin/python
#####################################################
#           looping
#       Name : Stacy Emmy
#       Date : 26 / 5 / 20.
#####################################################
for numbers in range(0,10):
    if(numbers %2 == 0):
        print(numbers)
#sum of even numbers between (0,20)
sum_numbers = 0
for numbers in range(0,20):
    if(numbers % 2 == 0):
        sum_numbers = sum_numbers + numbers
print(sum_numbers)

#product of all odd numbers between (0,20)
product = 1
for numbers in range(1,20):
    if(numbers % 2 == 1):
        product = product * numbers
print(product)

#calculate the factorial of 6!
product = 1
for numbers in range(1,7):
    product = product * numbers
print(product)
#calculate the factorial of 9!
product = 1
for numbers in range(1,10):
    product = product * numbers
print(product)

############################################
#while loop
num = 0
while num < 10:
    if (num % 2 == 0):
        print(num)
    num = num + 1
