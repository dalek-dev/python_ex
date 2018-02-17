# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 00:28:59 2018

@author: vict
"""

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#1
y = "Those who know %s and those who %s." % (binary,do_not)

print (x)
print (y)
# Esta linea imprime la variable x que contiene un parametro %d que es ingresado por si mismo
#2
print("I said: %r." % x)
#Esto imprime la utilizacion de una variable que llama a otras dos variables binary y do_not, dentro de otra variable
#3
print("I also said: '%s'." % y)

#se usa %r para depuracion, para obtener datos en bruto, y %s de string para mostrar a el dato a los usuarios

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#esta linea imprime una variable que dentro posee un parametro %r y que es usado por otra variable para mostrar False
#4
print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."
#está linea imprime una concatenacion de w y e
print (w + e) 