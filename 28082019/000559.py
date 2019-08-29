# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 00:07:41 2019

@author: johns
"""
import numpy as np #importa libreria

a = np.array([2,3,4])   #genera arreglo
print a #imprime variable

a = np.arange(1, 12, 2) #genera arreglo del 1 al 12interespaciados en 2
print a #imprime variable

a = np.linspace(1,12,6) #genera arreglo del 1 al 12 con los 6 elementos xdistanciados
print a #imprime variable

a = a.reshape(3,2) #cambia el formato del arregloa sociado a la variable a
print a #imprime variable

print a.size #imprime el tamanio de a

print a.shape #imprime las dinemciones de a

print a.dtype #imprime el tipo de datos dentro de a

print a.itemsize #imprime el tamanio de los datos dentro de a

b = np.array([(1.5, 2, 3), (4, 5, 6)]) #genera nuevo arreglo
print b #imprime variable

print a < 4 #imprime la verificacion de la inecuacion dentro del arreglo

print a * 3 #imprime la multiplicacion de los items dentro del arreglo

print a #imprime variable

a *= 3 #reasigna a la variable a el triple del valor anterior
print a #imprime variable

a = np.zeros((3, 4)) #genera arreglo de 0
print a #imprime variable
print a.dtype

a = np.ones((2, 3)) #genera arreglo de unos  dos corrias de 3 columnas
print a #imprime variable

a = np.ones(10) #genera arreglo de unos
print a #imprime variable

a = np.array([2, 3, 4], dtype = np.int16) #genera arreglos donde los numeros son int16
print a #imprime variable
print a.dtype
print a.itemsize

a= np.random.random((2, 3)) #genera arreglo con numeros aleatoresoentre 0 y 1
print a #imprime variable

np.set_printoptions(precision=2, suppress=True) #cambia la cantidad de decimales a mostrar dentro del arreglo
print a #imprime variable

a = np.random.randint(0, 10, 5) #genera 5 numeros enteros aleatoreso dentro del rango 0 a 10
print a #imprime variable
print a.sum() #operacion sobre arreglo
print a.min() #operacion sobre arreglo
print a #imprime variable
print a.max() #operacion sobre arreglo
print a.mean() #operacion sobre arreglo
print a.var() #operacion sobre arreglo
print a.std() #operacion sobre arreglo

a = np.random.randint(1, 10, 6) #vuelve a generar un arreglo con valores aleatoreos del 1 al 10, 6 valores
print a #imprime variable
a = a.reshape(3,2) #cambia las dimenciones del arreglo
print a #imprime variable
print a.sum(axis=1) #suma las filas del arreglo

print a.sum(axis=0) #suma las columnas del arreglo

# data = np.loadtxt("data.txt", dtype=np.unit8, delimiter=",", skiprows=1)