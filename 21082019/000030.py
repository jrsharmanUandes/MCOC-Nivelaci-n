a = [3, 10, -1] #crea una lista z la asocia a la variable a

print a         #imprime la lista asociada a a

a.append(1)     #agrega el valor 1 a la lista a

print a         #imprime la lista asociada a a

a.append("hello")   #agrega el str a la ultima posicion de la lista
print a         #imprime la lista asociada a a

a.append([1, 2])    #agrega la lista compuesta por los dos valores a la lisa a
print a         #imprime la lista asociada a a

a.pop()         #elimina el ultimo termino de la lista a
print a         #imprime la lista asociada a a

a.pop()         #elimina el ultimo termino de la lista a
print a         #imprime la lista asociada a a

print a[0]      #imprime el primer valor de la lista

print a[3]      #imprime el cuarto valor de la lista

a[0] = 100      #reemplaya el termino que se encuentra en la primera posicion de la lista por 100
print a         #imprime la lista asociada a a

b = ["banana", "apple", "microsoft"] #asocia la lista de str a la variable b

print b         #imprime la lista asociada a b

temp = b[0]     #asocia la variable temp al primer str de la lista b
b[0] = b[2]     #reemplaza el primer termino de la lista b por el tercero
b[2] = temp     #reemplaza el tercer termino de la lista b por el str asociado a la variable temp invirtiendo finalmente la lista
print b         #imprime la lista asociada a b

b[0], b[2] = b[2], b[0]     #forma simplificada de invertir la lista b, equivalente a los pasos anteriores, solo que escrito en una linea de codigo donde no es necesario guardar un termino
print b         #imprime la lista asociada a b
