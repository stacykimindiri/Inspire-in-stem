#!/usr/bin/python
#program to write numbers in reverse
num= 244
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //=10
print("reversed_num:" + str(reversed_num))