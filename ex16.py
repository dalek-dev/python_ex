# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:49:28 2018

@author: vict
"""
#importar el modulo 
from sys import argv

#values to unpack
script, filename = argv

#imprimir en pantalla el nombre del archivo
print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C)")
print ("If you do want that, hit RETURN")

#Ingresar una opcion para continuar o parar el proceso
input("?")
print ("Opening the file...")
#usar la variable target para alamacenar el nuevo archivo, y usamos 'w', para indicarle
#esta variable target borrara el archivo por completo existente gracias al parametro 'w'
target =  open(filename, 'w')

print("Truncating the file. Goodbye!")
#a la variable target se le borra la informacion por completo hasta donde se le de un parametro
#si no posee un parametro funcionará como el 'w' de open(filename, 'w')
target.truncate()

print("Now I'm going to ask you for three lines.")

#ingresamos nuevos datos en la variable line1
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

#escribimos y almacenamos la line1 en nuestro archivo generado target
target.write(line1)
#hacemos un salto de linea dentro del archivo
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3) 
target.write("\n")
print ("And finally, we close it.")
#cerrramos y guardamos el archivo de la variable target con la propiedad close()
target.close()

print ("Ingrese el dato %r de line1, %r de line2, %r de line3" % (
        line1,line2,line3)
)
