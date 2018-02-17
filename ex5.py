# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:46:06 2018

@author: vict
"""

name = 'victor miranda'
age = 25 #not a lie
height = 171 #centimetros
weight = 83 #kgr
inches=height*0.393701
libr=weight*2.20462
eyes = 'Blue'
teeth= 'White'
hair = 'Brown'

print ("Let's talk about %s." % name)
print ("He's %d inches tall." % height)
print ("He's %d pounds heavy." % weight)
print ("Actually that's not too heavy.")
#el formato %r permite que pueda ingresar cualquier tipo de dato
print ("He's got %s eyes and %s hair." % (eyes,hair))
print ("His teeth are usually %s depending on the coffee." % teeth)
#Se puede redondear un float con la propiedad round(numero,digitos_a_rendondear)
print ("Mi peso en pulgadas es %r, mi altura en libras es %r." % (round(libr,2),round(inches,2)))


#this line is tricky, try to get it exactly right
print ("If I add %r, %r, and %r I get %r" % (age, height,weight, age + height + weight))