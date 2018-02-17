# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:40:32 2018

@author: vict
"""

def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b +1

def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a - b +1

def multiply(a, b):
    print ("MULTIPLYING %d  * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(25, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

#A puzzle for the extra credit, type it in anyway
print("Here is a puzzle")

#usando la funcion add, siendo invocado varias veces por si misma
what = add(age, subtract(height,multiply(weight,divide(iq, 2))))

#imprimiendo la variable what
print ("That becomes: ", what, "Can we do it by hand?")