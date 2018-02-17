# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:42:40 2018

@author: vict
"""
def number_loop(a): 
    i = 0

    while i < a:
        print("At the top i is %d" % i)
        numbers.append(i)
        
        i += 8
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)


numbers = []

number_loop(6)

print("The numbers: ")

for num in numbers:
    print(num)