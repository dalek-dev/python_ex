# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:33:19 2018

@author: vict
"""
#importamos el argumento de la variable argv del sistema sys (modulos)
from sys import argv

#values to unpack
script, filename = argv

#el metodo open le dice al equipo que produzca un nuevo archivo de texto invocado de filename en este caso ex15_sample.txt
#en la misma carpeta donde se creo en este caso ex15.py
txt = open(filename)

print ("Here's your file %r: " % filename)
#imprimimos y leemos todo el archivo con read()
print (txt.read())

print ("Type the filename again: ")
#almacenamos un nuevo texto ingresandolo dentro de input
file_again = input("> ")

#se guarda en una variable txt_again con la propiedad open, un archivo nuevo
txt_again = open(file_again)

#Imprime el archivo y muestra el contenido tal cual sin modificarlo
print (txt_again.read())

