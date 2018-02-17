# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:31:00 2018

@author: vict
"""

class Parent(object):
    def implicit(self):
        print( "PARENT implicit()")
        
class Child(Parent):
    pass #pass se comporta como un bloque vacio

dad = Parent()
son = Child()

dad.implicit()
son.implicit()