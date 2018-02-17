# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:59:12 2018

@author: vict
"""

class Parent(object):
    
    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD, AFTER PARENT altered()")
        
dad = Parent()
son = Child()

dad.altered()
son.altered()