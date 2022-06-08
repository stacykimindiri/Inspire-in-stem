#!/usr/bin/python
#####################################################
#       Dictionaries
#       Name : Stacy Emmy
#       Date : 23 / 5 / 20.
#####################################################
# A dictionary is a collection of key value pair
# Syntax: dictionary = {"key":"value"}
# Initializing dictionaries
student = {"Name":"Stacy","Age":"18","Gender":"female"}

#Accessing values in dictionaries
print(student["Name"])
print(student["Age"])
print(student["Gender"])

#Adding key values to a pair in dictionaries
student["Id.No"] = "5044182"
student["Hobby"] = "Nairobi"
student["Club"] = "none"
print(student)

#Empty dictionary -- student ={}
student = {}
student["favourite_food"] = "chicken roll"
student["Home_city"] = "Nairobi"
student["favourite_artist"] = "Doja Cat"
print(student)

#Modifying the values  --to change
student["Name"] = "Wambui"
student["Age"] = "20"
print(student)

#deleting a key value from a dictionary
del student["favourite_food"]
print(student)


#################################################################
# Syntax: dictionary = {'key':'value'}
#list_names = ['Stacy','Emmy']
colours = {'colour':'red'}
vehicle = {'type':'toyota','plate_number':'KYZ45'}
#print(type(colours))##we use the type methode to read the data type of a string
print(vehicle["type"])
print(vehicle["plate_number"])
print(vehicle["type"],vehicle["plate_number"])
######################################################################################
person = {'Name':'Stacy','Address':'Embakasi','Gender':'Female','Number':'0701333684'}
print(person)
person["fav_colour"] = "Red"
print(person)
print(person['Name'],person['fav_colour'],person['Number'])
del person['Number']
print(person)

#############################################
#Looping in dictionary
person = {
    'Name':'Stacy',
    'Address':'Embakasi',
    'Gender':'Female',
    'Number':'0701333684'
    }
print(person)

for key,value in person.items():
    print(f"Name{value}:{key}")

# Using the get method to access the values in a dictionary
print(person.get('password','The key password is non existent'))
###############################################################
#           lists in dictionaries
Stacy_fav_food = ['ugali','meat','vegetabls']
Emmy_fav_food = ['rice','meatballs','pizza']
fav_food = {
    'stacy':['ugali','meat','vegetabls'],
    'emmy':['rice','meatballs','pizza']
    }
print(fav_food)
for key,value in fav_food.items():
    print(f"{key}:{value}")