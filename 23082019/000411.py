# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:05:52 2019

@author: johns
"""

given_list = [5, 4, 4, 3, 1, -2, -3, -5] #define la variable givenlist con una lista 

total3 = 0  # define la variable total3 igual a 0
i = 0   #define la variable i igual a cero
while i < len(given_list) and given_list[i] > 0:    #verifica si el termino i-esimo de la lista asociada a given_list es mayor a 0 y si i no es mayor al largo de la lista para iniciar el loop
    total3 += given_list[i]     #acumula la suma de los elementos i-esimos de la lista given
    i += 1 #suma uno a la variable i cada vez que recorre el loop
    
print total3 #imprime total3



### mismo ejemplo que el anterior pero usando for loop
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5] #define la variable givenlist con una lista 
total4 = 0 #define la variable
for element in given_list2: #recorre los elementos de la lista
    if element <= 0:    #verifica si element es menor o igual que 0
        break   #termina de recorrer los loop y sale de la funcion for
    total4 += element #acumula resultados
print total4 #imprime la variable



