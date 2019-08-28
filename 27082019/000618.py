# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:29:58 2019

@author: johns
"""


import numpy as np  #importa libreria
from skimage import io #imprime la libreria skimage

photo = io.imread('frame_93600.png')    #lee la imagen
print type(photo)   #imprime que tipo de dato asociado a la variable photo
print photo.shape   #imprime las dimenciones de la variable photo

import matplotlib.pyplot as plt #importa la libreria 
plt.imshow(photo)   #imprime la imagen asociada a la matriz de photo
plt.show()          #plotea todo
plt.imshow(photo[::-1])     #invierte verticalmente la matriz
plt.show()          #plotea todo
plt.imshow(photo[:, ::-1])  #invierte horizontalmente la matriz
plt.show()          #plotea todo
plt.imshow(photo[50:150, 150:280])
plt.show()          #plotea todo
plt.imshow(photo[::2, ::2])
plt.show()          #plotea todo

print photo
photo_sin = np.sin(photo)
print photo_sin


### imprime distintos datos del arreglo
print np.sum(photo)     
print np.prod(photo)    
print np.mean(photo)
print np.std(photo)
print np.var(photo)
print np.min(photo)
print np.max(photo)
print np.argmin(photo)
print np.argmax(photo)

z = np.array([1, 2, 3, 4, 5])  #crea arreglo
print z<3 #verifica que valores del arreglo cumplen
print z>3 #verifica que valores del arreglo cumplen
print z[z>3] #estrae los valores que cumplen

photo_masked = np.where(photo > 100, 255, 0) #reemplaza los valores mayores a 100 con 255 y los menores con 0

plt.imshow(photo_masked)
plt.show()          #plotea todo


### Crea dos nuevos arreglos
a_array = np.array([1,2,3,4,5])
b_array = np.array([3,7,8,9,10])


### Ecuaciones con los arreglos
print a_array + b_array
print a_array + 30
print a_array * b_array
print a_array * 10


plt.imshow(photo[:,:,0].T) #rota y cambia lso valores de la imagen
plt.show()          #plotea todo

x = np.array([2, 1, 4, 3, 5]) #define nuevo arreglo
print np.short() #imprime arreglo ordenado
