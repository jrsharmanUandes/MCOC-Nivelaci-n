# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:41:22 2019

@author: johns
"""

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5] #define la variable givenlist con una lista 

total5 = 0 #define la varaible
i = 0 #define la variable
while True: #inicia con el loop
    total5 += given_list2[i]    #acumula los valores que se van entregando por el i-esimo termino 
    i += 1  #acumula i sumandole 1
    if given_list[i] <= 0:  #verifica si el i-esimo elementod e la lista es menor o igual a 0
        break #termina el loop saliendo del while

print total5 #imprime la variable