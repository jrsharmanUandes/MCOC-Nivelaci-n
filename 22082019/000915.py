# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:44:25 2019

@author: johns
"""

for i in range(1,100):      #recorre la lista conformada por todos los valores entre 1 y 99 asociandoselos a la variable i
    if i % 3 == 0 and i % 5 == 0:   #comprueba si i es multiplo de 3 y de 5
        print i, " is multiple of 3 and 5"  # imprime en caso de que cumpla la conedicion
    elif i % 3 == 0:            # en caso de no cumplir lo anterior verifica si es multiplo de 3
        print i, " is multiple of 3"    #en caso de cumplir el elif imprime el valro de i y el str
    elif i % 5 == 0:            # en caso de no cumplir lo anterior verifica si es multiplo de 5
        print i, " is multiple of 5"    #en caso de cumplir el elif imprime el valro de i y el str
    else:                       #en caso de no cumplir lo anterior sigue con el loop
        continue                #sigue con el loop