#!/usr/bin/python
#####################################################
#       Name : Stacy Emmy
#####################################################
import random
print('Welcome to our password generator')
character = 'kdb17'
#ask number of pw
number_of_passwords=int(input("How many are the passwords:"))
#ask the user for pw length
length_of_password=int(input("How long are the passwords"))
print('/Here are your passwords.')
for password in range (number_of_passwords):
    passwords=''
    for c in range(length_of_password):
        password+=random.choice(character)
    print(password)