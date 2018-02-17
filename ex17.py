# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:19:49 2018

@author: vict
"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("copying from %s to %s" % (
        from_file,
        to_file))

#we could de these two on one line too, how?
in_file = open(from_file)
#permite que tengamos permisos de escritura nuestra variable in_file
in_data = in_file.read()

#el metodo len() nos permite saber la longitud en bytes del archivo
print("The input file is %d bytes long" % len(in_data))
#exists permite saber si el archivo existe en el directorio, si es asi es True, en caso contrario False
print ("Does the output file exists? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#nos permite crear el archivo to_file, vaciandolo con el parametro 'w'
out_file = open(to_file, 'w')
#Nos permite escribir los datos de in_data en out_file
out_file.write(in_data)

print ("Alright, all done.")

# cerramos el archivo de out_file
out_file.close()
#cerramos y guardamos los cambios el archivo de in_file
in_file.close()