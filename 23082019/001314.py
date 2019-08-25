# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:43:50 2019

@author: johns
"""

given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7] #define la variable givenlist con una lista 
given_list3.sort()  #ordena de menor a layor la lista anterior de tal forma que los numeros negativos queden en la primera parte de ella
print given_list3 #imprime la nueva lsita ordenada

total6 = 0 #define la variable
i = 0   #define la variable
while True: #inicia loop
    if not given_list3[i] < 0: #verifica si el i-esimo elemento de la lista NO es menor a 0
        break #termina el loop saliendo del while
    total6 += given_list3[i] #acumula los valores
    i += 1 #acumula + 1 a la varaible i
    
print total6 #imprime la variable