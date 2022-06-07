#!/usr/bin/python
#            Modules 
#        Name : Stacy Emmy
#        Date :  6/ 6 / 20.
import operations
from student import student

from teachers import Teachers

from classes import Classes

print(operations.add_numbers(8,9))
print(operations.subtract_numbers(6,3))
print(operations.multi_numbers(45,8))
print(operations.divide_numbers(67,3))


new_student = student("Emmy","singing",2004)

student.greet_student()

new_teacher = Teachers("Mr John",12467,"Literature",8900)
new_teacher.get_tsc_no()

new_class = Classes("fifty students","south wing")
new_class.get_wing()