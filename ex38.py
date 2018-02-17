# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:28:22 2018

@author: vict
"""

ten_things = "Apple Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #añade un dato a la lista, comenzando por la parte final de la lista more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one) #añade un dato a la lista
    print("There's %d items now." % len(stuff)) #muestra la longitud de la variable stuff, en este caso es una lista
    
print ("There we go: ", stuff)

print("Let's do some things with stuff.")

#imprime el primer dato de la lista
print(stuff[1])
#utiliza el ultimo dato de la lista 
print(stuff[-1]) #whoa! fancy
#pone el dato al final de la lista
print(stuff.pop())
#join une las cadenas con el valor que desee '' o '#'
print(''.join(stuff)) #what? cool!
print('#'.join(stuff[3:5])) #super stellar!