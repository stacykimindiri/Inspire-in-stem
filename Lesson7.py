#!/usr/bin/python
#creating loops
school = ["Joy" , "Hope" , "Mercy" , "Happy"]
pupil = ["Peace" , "Grace" , "Stacy" , "Emmy"]


###########################################################################
#Hard way
print(f"i am {pupil[0]} and i school at {school[0]}")
print(f"i am {pupil[1]} and i school at {school[1]}")
print(f"i am {pupil[2]} and i school at {school[2]}")
print(f"i am {pupil[3]} and i school at {school[3]}")
#Easier way
for pupil in pupil:
    print(f"Hello i am pupil { pupil }")


#############################################################################
#To access a specific item from a list --[-1]
print(school[-1])

#############################################################################
print("number\tSquare")
print("============")
for number in range(0,9):
    print(number)
    print("\t")
print(number**2)
