# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:51:13 2018

@author: vict
"""

#this one is like your scripts with argv
#Para decirle a python que vamos a usar una funcion necesitamos usar 'def'
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
   
    

#This just tales one argument
def print_one(arg1):
    print ("arg1: %r" % arg1)
    
#this one takes no arguments
def print_none():
    print ("I got nothin' .")
    
print_two("victor", "miranda")
print_two_again("victor", "miranda")
print_one("First!")
print_none()
