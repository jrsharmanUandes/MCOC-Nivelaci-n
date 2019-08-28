# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:02:10 2019

@author: johns
"""

import numpy as np  #importa libreria
a = np.zeros(3)     #crea un arreglo de 3 ceros
print a             #imprime variable

z = np.zeros(10)    #crea arreglo con 10 ceros

print z.shape       #imprime las dimenciones de z
z.shape = (10, 1)   #cambia las dimenciones de z
print z             #imprime variable

z = np.ones(10)     #crea un arreglo de 10 unos
print z             #imprime variable

z = np.empty(3)     #crea un arreglo vacio, de 3 espacios
print z             #imprime variable

z = np.linspace(2, 10, 5) #crea un arreglo desde el numero 2 al 10 con 5 elementos
print  z            #imprime variable

z = np.array([10, 20]) #crea un arreglo con los valores  10 y 20
print z             #imprime variable

a_list = [1, 2, 3, 4, 5, 6, 7]  #crea una lista con estos valores
z = np.array([a_list])  #crea un arreglo a partir de la variabla a la que esta asociada la lista definida anteriormente
print z             #imprime variable
print type(z)       #imprime el tipo de dato asociado a variable z

b_list = [[9, 8, 7, 6, 5, 4, 3], [1, 2, 3, 4, 5, 6, 7]] #crea una lista con dos listas en su interior
z = np.array([b_list]) #crea un arreglo a partir de la variabla a la que esta asociada la lista definida anteriormente
print z             #imprime variable          
print z.shape       #imprime las dimenciones de la varaible z

np.random.seed(0)   #crea una semilla a partir de la cual genera lso valores del random
z1 = np.random.randint(10, size=6)  #genera una lista con un margen superior de 10 valores enteros y aleatorios. 6 valores en total
print z1            #imprime variable

print z1[0]         #imprime el primer valor del arreglo
print z1[0:2]       #imprime un sub arreglo desde el 0 al 2 valor
print z1[-1]        #imprime el ultimo valor de la lista



