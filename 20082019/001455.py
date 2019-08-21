def convert(mile):	#define a funcion para convertir millas a km
    print('La distancia en millas que usted deseaba convertir a kilometros es: ') 	#imprime el str
    print(mile)		#imprime el valor asociado a la variable mile dentro de la funcion
    print('Y su equivalente en km es: ') 	# imprime str
    print(mile * 1.6) 	# imprime la convercion

miles = 5		# define la variable miles con un int
km = convert(miles)	# llama la funcion entregandole el int de asociado a miles