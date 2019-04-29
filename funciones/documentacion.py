#Sacar provecho a nuestra documentación.

"""
Almacenamos las funciones dentro de nuestro diccionario, 
posteriormente iteramos los elementos del diccionario 
y en cada iteración imprimimos la documentación
"""

def suma(a, b):
	"""Función suma (documentación)"""
	return a + b

def resta(a, b):
	"""Función resta (documentación)"""
	return a - b

opciones = {'a' : suma, 'b': resta}

print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
	mensaje = '{}) {}'.format(opcion, funcion.__doc__)
	print(mensaje)

opcion = input("Opción : ")