# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:28:12 2018

@author: vict
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
    \t* Cat food
    \t* Finishies
    \t* Catnip\n\t* Grass
    """
    
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

while True:
    for i in ["/","-","|","\\"]:
        print("%s\r" % i)