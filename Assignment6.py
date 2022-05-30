#!/usr/bin/python
#########################################
#       Geometric progression
a = int(input("Enter the first number"))
r = int(input("Enter the common ratio"))
n = int(input("Enter the value of n "))
for i in range(1,n + 1 ):
    t_n = a * r**(i -1)
    print(t_n)
sum_n2 = (a*(1 - (r^n + 1))) / (1-r)
print("The sum of geometric progression:" ,sum_n2)