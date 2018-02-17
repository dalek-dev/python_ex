# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 02:15:44 2018

@author: vict
"""

from sys import argv

script, input_file = argv

# f es una variante, es un parametro representativo del archivo
def print_all(f):
    print (f.read())
    
#seek nos permite movernos a una posicion en el archivo, si es 0, nos posicionaria al comienzo del archivo
#la funcion seek utiliza bytes no lineas, por eso usa el byte 0, el primer byte en el archivo
def rewind(f):
    f.seek(0)

#cada vez que se usa readline() se está leyendo una líne adel archivo y moviendo la lectura
#hacia la derecha después del salto \n termina la lectura del archivo
#redline es una funcion que escanea cada byte en el archivo hasta que encuentra \n, luego se detiene para devolver
#lo que encontro hasta ahora
#el archivo nombrado f por la funcion, es el que va mantener la posicion despues de cada llamada de la 
#funcion para que siga leyendo cada linea
def print_a_line(line_count, f):
    print (line_count, f.readline())

#abrimos el archivo de input_file, y lo almacenamos en la variable current_file
current_file =  open(input_file)

print("First let's sprint the whole file:\n")

print_all(current_file)

print ("Let's print three lines:")

current_line=1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)