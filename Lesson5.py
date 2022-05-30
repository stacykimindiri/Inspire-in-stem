#!/usr/bin/python
# methods
name = "Stacy Emmy"
user_name = "Ada Lovelace"
age = 18
person = "i am " + str(name) +"and my age is " + str(age)
print(person)

#person = "i am " + str(name) +"and my age is " + str(age)
#print("i am " + str(name) + "and my name is " + str(age))
print("My name is {} and i am {} years old " .format(name,age))

# the format()method
#print("My name is {} and i am {} years old " .format(name,age))
#newline \n and tab\t
#tab \t
print("Monday\tTuesday\wednesday\tThursday\tFriday")
#new line \n
print("kisumu\nnairobi\nmombasa\nnaivasha\n")

#print("My name \t {name} \n and i am {age} years old ")
print(user_name.lstrip())

msg = '''QRST126XDG MPESA confrimed
        you have recieved Ksh 2300 from
        Stacy Emmy 18th May 2022
        safaricom transpare for you
        '''
print(msg)
txt = '''Holla i am Stacy Emmy
            I come from Nairobi,
            '''
print(txt)

#removing letters from a word
city = "Nairobi"
print(city[:5])
print(city[2:])
print(city[1:])

# changing the cases
f_name = "stacy emmy " #small letters
#.upper()convert to upper case
print(f_name.upper())
s_name = "STACY EMMY"
#.lower()convert to lower case
print(s_name.lower())

#concatination - converting from one data type to another
#int ->float float(x)
#float ->int int(x)
number = 6
print(str(number))
x = 4 # x is an integer
print(float(x))
y = 3.24 
print(int(y))

#replacing characters i words with other characters
f_name = "Stacy"
s_name = "Emmy"
full_name = f_name + s_name
print(full_name)
name = "Stacy Emmy"
print(name.replace('y','e'))

#The split method
msg = "Hello from Stacy Emmy how are you " #separates words
print(msg.split())
print(len(msg)) # determines the number of characters in words