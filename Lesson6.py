#!/usr/bin/python
# learning about a list
motorcycle_owner = "Stacy Emmy"
plate_number = ["H234" , "S675" , "Y960"]
motorcycle = ["Honda" , "Suzuki" ,"Yamaha"]
print(motorcycle) #creating a list[]

#accessing an item from a list using git index
print(motorcycle[1])

#changing an element in a list
motorcycle[2] = "Bugatti"
print(motorcycle) # replacing

#adding an element to list --append
motorcycle.append("Isuzu ")
print(motorcycle)
#assigning number plates
print(motorcycle[0],plate_number[0],motorcycle[1],plate_number[1])

#deleting an item from a list --delete
del motorcycle[2]
print(motorcycle)
motorcycle.remove("Suzuki")
print(motorcycle)

#popped_motorcyle = motorcycle.popp()
#print(popped_motorcyle)

#print a statement
print("My name is " + motorcycle_owner + "and i own " + motorcycle[0] + plate_number[0])
print(f"My name is{motorcycle_owner} and i own {motorcycle[0]}, {plate_number[0]}")
