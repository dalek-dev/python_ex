# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:05:47 2018

@author: vict
"""

the_count = [1,2,3,4,5]
fruits = ['apples','orange','pears','apricorts']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the first kind of for-loop goes through a list

for number in the_count:
    print("This is count %d" % number)
    
#same as above
for fruit in fruits:
    print("A fruit %s" % fruit)
    
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
    print("I go %r" % i)
    
#we can also build lists, first start with an empty one
#listado vacio de elements
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list." % i)
    #appends is a function that lists understand
    #append es usado para ingresar los elementos dentro de elements
    elements.append(i)
    
#now we can print them out too
#recorrido de los elementos dentro de elements
for i in elements:
    print("Element was: %d" % i)