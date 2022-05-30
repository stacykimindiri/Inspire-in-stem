#!/usr/bin/python
#a program to withdraw ksh 25,000 if account balance is ksh 100,000 to 200,000 and 30% if account balance is between ksh 500,000 and 1m
# and above 1m deduct ksh 15,000
account_balance =int(input("Enter account balance "))
if (int(account_balance)> 100000 and int(account_balance) <200000):
    new_balance = account_balance - (25000)
    #new_balance -=25000
    print("we have deducted 25000\n")
elif (int(account_balance)>500000 and int(account_balance)<1000000):
    new_balance = account_balance - (0.3 * account_balance)
    print("we have deducted 30%")
elif (int(account_balance) > 1000000):
    new_balance = account_balance - (15000)
    print("we have deducted 15000 ")
    print(f"Your account balance is {new_balance}")
else:
    print("No deductions done")