# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:32:00 2019

@author: johns
"""

b = [20, 10, 5]     #crea la lista y la asocia a la variable b

total = 0

for e in b:         # recorre los elementos de la lista b y lso asocia a la variable e
    print e         #imprime lo asociado a e
    total = total + e   #suma cada vez que recorre el loop a la variable total el valor que se encuentra asociado a e

print total     #imprime el valor final de total que corresponde a 0 mas la suma de todos los valores en la lista

c = list(range(1,5))    # crea una lista con los valores enteros dentro de la lista: 1, 2, 3, 4
print c         #imprime la lista c



total2 = 0  #define la varaible total2
for i in range(1, 5): #recorre el loop entregandole al la variable i los valores dentro del rango
    total2 += i         #forma reducida de sumarle a total si mismo y el valor de i
print total2            # imprime el valor final de total2


print list(range(1,8))  #imprime la lista con los valores que se encuentran en el rango 1 a 7
total3 = 0          #define la variable total3 igual a 0
for i in range(1, 8):   #recorre una lista asociando a la variable i los valores del rango 1,7
    if i%3 == 0:        #verifica si la varaible i toma un valor multiplo de 3
        total3 += i     #en caso de tomar un multiplo de 3 le suma este a la variable total3
print total3            #imprime el valor final que toma la variable total3
 