# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:00:59 2018

@author: vict
"""
#
#import fbchat
#from getpass import getpass
#username=str(input("Usuario: "))
#client = fbchat.Client(username,getpass())
#no_of_friends=int(input("Numero de amigos: "))
#for i in range(no_of_friends):
#    name=str(input("Nombre de mi amigo elegido: "))
#    friends=getUsers(name) #return a list of names
#    friend=frinds[0]
#    msg=str(input("Escribe un mensaje para tu amigui:  "))
#    sent=client.send(name.uid, msg)
#    if sent:
#        print("Mensaje enviado!")


import fbchat

client = fbchat.Client("victor.mirandadiniz", "biologia")

friends = client.getUsers('')  # return a list of names
friend = friends[0]
sent = client.send(friend.uid, "Your Message")
if sent:
    print("Message sent successfully!")
