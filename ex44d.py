# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:06:15 2018

@author: vict
"""

class Parent(object):
    def override(self):
        print("PARENT override()")
        
    def implicit(self):
        print("PARENT  implicit()")
    
    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        print("CHILD, AFTER PARENT altered()")
        super(Child,self).altered()
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()