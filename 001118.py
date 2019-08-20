# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:43:57 2019

@author: johns
"""

a = 1           #Aesigna 1 a variable a
b = 2           #Aesigna 2 a variable b
if a < b:       #Verifica si a es menor que b
    print 'a is less than b'                # imprime str
    print 'a is definetrly less than b'     # imprime str
print 'Not sure if a is less than b'        # imprime str fuera de las condiciones


c = 3           #Asigna 3 a variable c
d = 4           #Asigna 4 a variable d
if c < d:       #Verifica si c es menor que d
    print 'c is less than d'                # imprime str
else:           # En caso de no cumplir condicion sigue con esta
    print 'c is NOT less than d'            # Imprime str
    print "I don't rhink c is less than d"  # Imprime str
print 'outside the if block'                # Imprime str fuera de las condiciones

e = 10          #Asigna 10 a variable e
f = 8           #Asigna 8 a variable f
if e < f:       #Verifica si e es meor que f
    print 'e is less than f'                # Imprime str
elif e == f:    #En caso de no cumplir anterior verifica si e es igual a f
    print 'e es equal to f'                 # Imprime str
elif e > f + 10:    #En caso de no cumplir anterior verifica si e es en 10 mayor que f
    print 'e is greater than f by more than 10'     # Imprime str
else:           # En caso de no cumplir condiciones sigue con esta
    print 'e is not less than f'            # Imprime str
    
g = 9           #Asigna 9 a variable g
h = 8           #Asigna 8 a variable h
if g < h:       #Verifica si g es menor a h
    print 'g is less than h'                # Imprime str
else:           #En caso de no cumplir condicion sigue
    if g == h:  #Verifica si g es igual a h
        print 'g is equal to h'     #imprime str
    else:       #si no cumple lso anteriores
        print 'g is greater than h' #imprime str
        
        
name = 'YK'     #asigna str a variable name
height_m = 2    # asigna 2 a variable heigh_m
weight_kg = 90  #asigna 90 a variable weight

bmi = weight_kg / (height_m ** 2) # divide la masa en el cuadrado de la altura
print 'bmi: ' #imprime str
print bmi #imprime valor entregado por ecuacion anterior
if bmi < 25: #condicion si bmi es menor a 25
    print name #imprime variable nombre
    print 'is not overweight' #imprime str
else: #en caso de no cumplir sigue con esto
    print name #imprime variable nombre
    print 'is overweight' #imprime str