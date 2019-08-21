#BMI calculator

### define las variables
name1 = 'YK'
height_m1 = 2
weight_kg1 = 90

name2 = "ZK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160


### FUNCIONES ###
def bmi_calculator(name, height_m, weight_kg): 	#define la funcion para calcular bmi que toma 3 parametros
    bmi = weight_kg / (height_m**2) 		#calcula el bmi y lo asocia a una variable bmi
    print('bmi: ') 				# Imprime str
    print(bmi) 					# Imprime el valor calculado asociado a bmi
    if bmi < 25: 				# verifica si bmi es menor a 25
        return name + 'not overweight' 		#devuelve si la persona name no tiene sobrepeso
    else: 					# En caso de no cumplir la condicion de < 25 sigue con esto
        return name + 'is overweight'		# devuelve el nombre en str mas el str escrito en ''

result1 = bmi_calculator(name1, height_m1, weight_kg1) #llama la funcion entregandole los valores definidos en la primera parte
result2 = bmi_calculator(name2, height_m2, weight_kg2) #llama la funcion entregandole los valores definidos en la primera parte
result3 = bmi_calculator(name3, height_m3, weight_kg3) #llama la funcion entregandole los valores definidos en la primera parte


print(result1) 	#imprime la variable que definimos anteriormente
print(result2)	#imprime la variable que definimos anteriormente
print(result3)	#imprime la variable que definimos anteriormente

