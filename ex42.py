# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:02:46 2018

@author: vict
"""

#Animal is-a object (yes, sort of confusing)look at the extra credit
class Animal(object):
    pass

## has-a
class Dog(Animal):
    
    def __init__(self,name):
        ## has-a
        self.name = name
        
## has-a
class Cat(Animal):
    
    def __init__(self, name):
        ## has-a
        self.name = name
        
## is-a
class Person(object):
    
    def __init__(self, name):
        ## has-a
        self.name = name
        
        ##person has-a pet of some kind
        self.pet = None
        
## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmmm what is this strange magic?
        super(Employee,self).__init__(name)# se utilza para heredar atributos de una clase padre.
        ## has-a
        self.salary = salary ##se instancia a si misma
        
        
## is-a
class Fish(object):
    pass ##se esta funcion cuando qieres que continue el proceso, ya que posteriormente será reemplezado por codigo

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

##rover is-a dog
rover = Dog("Rover")


## is-a
satan = Cat("Satan")

## is-a
mary = Person("Mary")


## has-a
mary.pet = satan

## is-a
frank = Employee("Frank",120000)

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()

