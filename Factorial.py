#!/usr/bin/python
#####################################################
#           Factorials
#       Name : Stacy Emmy
#       Date : 27 / 5 / 20.
#####################################################
number = int(input("Enter number"))
factorial = 1
if number < 0 :
    print("Factorial of negative numbers does not exist")
elif number == 0 :
    print("Factorial of 0 is equal to 1")
else :
    for i in range(1,number + 1):
        factorial = factorial * i 
print("factorial of the number is :",factorial)
