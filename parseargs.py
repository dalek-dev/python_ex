# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:40:18 2018

@author: vict
"""

import argparse

#argumento parser
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+')
#argumento posicional y opcional, que posee una descripcion
parser.add_argument('-f', '--foo', help='foo help')
#argumento posicional y opcional, que posee una descripcion
parser.add_argument('-b', '--bar', help='bar help')
#argumento posicional y opcional, que posee una descripcion
parser.add_argument('-z', '--baz', help='baz help')
#argumento posicional, y opcional que una accion
parser.add_argument('-t', '--turn-on', action='store_true')
#argumento posicional, y opcional que una accion
parser.add_argument('-x', '--exclude', action='store_false')
#argumento posicional, y opcional que una accion
parser.add_argument('-s', '--start', action='store_true')
#Parseo de argumentos, parsear significa hacer un recorrido de la base de datos
args = parser.parse_args()

#imprime la variable args
print(args)