# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:34:40 2018

@author: vict
"""

class Parent(object):
    
    def override(self):
        print("PARENT override()")
        
class Child(Parent):
    def override(self):
        print("CHILD override()")
        
dad = Parent()
son = Child()

dad.override()
son.override()