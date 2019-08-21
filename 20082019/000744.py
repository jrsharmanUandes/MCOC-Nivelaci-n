def function3(x,y):	#define la funcion que accepta dos parametros
    return x + y 	# devuelve la suma de lso dos terminos

e = function3(1,2) 	#de la a la variable e el valor entregado por la funcion al recibir el 1,2
print(e) 		# imprime la variable e

def function4(x): 	#define la funcion acceptando solo un perimetro
    print(x) 		#imprime el valor x dentro de la funcion
    print('still in this function') 	#imprime el str
    return 3*x 		#funcion devuelve 3*x

f = function4(4) 	#define la variable f con la funcion4 entregandole el perimetro 4
print(f)		#imprime la variable f
