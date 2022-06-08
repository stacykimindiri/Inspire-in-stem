#!/usr/bin/python
#           Fuctions
#        Name : Stacy Emmy
#        Date : 31 / 5 / 20.
# Functions is a block of code which gets executed together
# Initializing functions/definition of a function
def say_hello(): 
    print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    print(z)
# Calling functions
say_hello()

def bark():
    print("Dogs bark woof woof")
bark()
def moo():
    print("Cows moo")
moo()
def hiss():
    print("Snakes hiss ssss")
hiss()

#############################################################
# Function parameters
# A function to add numbers
def add_numbers(x,y):
    sum_nums=x+y
    print("The sum of the numbers is:",sum_nums)
add_numbers(40,50)
add_numbers(100,400)
add_numbers(1,4)
# A function to multiply numbers
def multi_numbers(x,y):
    prod_numbers=x*y
    print("The product of numbers is:",prod_numbers)
multi_numbers(20,3)
multi_numbers(50,70)


#passing a list in a funtion
def greet_friends(names):
    for name in names:
        msg("Hello "+ name.title()+" !")
        print(msg)
friends=['Bob','Wise','Gadson']
greet_friends(friends)

