#!/usr/bin/python
#####################################################
#       Name : Stacy Emmy
#       Date : 30 / 5 / 20.
#program to write numbers in reverse
#######################################################
num= 244
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //=10
print("reversed_num:" + str(reversed_num))
#######################################################
number = 9605
reversed_number=str(number)[::-1]
if type(number) == float:
    reversed_number==float(reversed_number)
elif type(number)==int:
        reversed_number=int(reversed_number)
print(f"The reversed number is {reversed_number}.")