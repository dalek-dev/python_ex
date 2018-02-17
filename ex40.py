# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:41:22 2018

@author: vict
"""

class Song(object):
    #constructor del obejeto
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    #clase sing_me_a_song
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
happy_bday = Song(["Happy birthday to you",
                        "I don't want to get sued",
                        "So I'll stop right there"])
    
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
    
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()