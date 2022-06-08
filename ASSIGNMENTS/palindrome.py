#!/usr/bin/python
#####################################################
#       Name : Stacy Emmy
#       Date : 8/6/2022
#####################################################
n=int(input("Enter number"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(f"The number {temp} is a palindrome")
else:
    print(f"The number {temp} isn't a palindrome")

#######################################################

