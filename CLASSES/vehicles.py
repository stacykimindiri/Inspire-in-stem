#!/usr/bin/python
#####################################################
#       Name : Stacy Emmy
#####################################################
#create a variable class
class vehicle:
    def __init__ (self,_mileage,_maxspeed):
        self._mileage=_mileage
        self._maxspeed=_maxspeed
audi=vehicle(420,90)
mercedes=vehicle(680,120)
print(audi.maxspeed,audi.mileage)
print(merceded.maxspeed,mercedes.mileage)