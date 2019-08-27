# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:55:49 2019

@author: johns
"""

d = {}      #crea un diccionario
d["George"] = 24    #asocia al nombre el valor 24
d["Tom"] = 32       #asocia al nombre el valor 32
d["Jenny"] = 16     #asocia al nombre el valor 16

###imprime  los valores asociados a los nombres
print d["George"]   
print d["Tom"]
print d["Jenny"]


d["Jenny"] = 20     #asocia un nuevo valor al nombre Jenny
print d["Jenny"]    #imprime el valor asociado a este nombre
d[10] = 100         #asocia al nombre 10 un vamor 100
print d[10]         #imprime el valor asociado a este nombre

for key, value in d.items(): #recorre todo el diccionario aosciando a las variables key y value los nombres y los valores asociados a estos
    #Imprime los valores asocaidos a las variables
    print "key:"
    print key
    print "value:"
    print value
    print ""