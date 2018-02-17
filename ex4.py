# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:59:25 2018

@author: vict
"""
#asignamos un 100 a la variable cars
cars = 100
#asignamos space_in_a_car un número flotante
space_in_a_car = 4.0
#asignamos 30 a la variable drivers
drivers = 30
#asignamos 90 a passengers
passengers = 90
#restamos la variable cars de la variable drivers
cars_not_driven = cars - drivers
#asignamos los valores de drivers a cars_driven
cars_driven = drivers
#asignamos cars_driven * space_in_a_car a carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print ("There are",cars,"cars available")
print ("There are only",drivers,"drivers available")
print ("There will be",cars_not_driven,"empty cars today")
#si variamos el tipo de dato de nuestra variable floante a entero, el resultado de carpool_capacity, será entero, ya no flotante
print ("We can transport",carpool_capacity,"people today")
print ("We have",passengers,"to carpool today.")
print ("We need to put about",average_passenger_per_car,"in each car.")
