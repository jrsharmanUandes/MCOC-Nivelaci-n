# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:05:50 2019

@author: johns
"""

total = 0   #define la variable total 
for i in range(1, 5):   #recorre la lista conformada por los numeros enteros dentro del range sin incluir en ultimo definiendo con estos la variable i
    total += i  #le suma la variable i a la variable total y la va acumulando
print total     #imprime la variable total

total2 = 0  #define la variable total2
j = 1   #define la variable j
while j < 5:    #revisa si j es menor a 5  e inicia el loop
    total2 += j     #acumula el valor j a total2
    j +=1   #acumula +1 cada vez que recorre el loop
print total2    #imprime el valor asociado a la variable total2

 