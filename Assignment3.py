#!/usr/bin/python
#program that gets user input -the if function
age = input("what is your age?")
account_balance = 0
if (int(age) > 25) and (int(age)< 30):
    account_balance = account_balance + 10000
    print("confirmed you have recieved ksh 10,000")
else:
    print("sorry no money for you")

