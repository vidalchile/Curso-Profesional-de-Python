# ejercicios-2.py
# -*- coding: utf-8 -*-

"""
Dado un diccionario, el cual almacena las calificaciones de un alumno, 
siendo las llaves los nombres de las materia y los valores las calificación, 
mostrar en pantalla el promedio del alumno
"""
calificaciones 	= {"calculo":10, "dibujo":5, "etica":4}
print("Promedio alumno: ", sum(calificaciones.values()) / len(calificaciones.values()))

"""
A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.
"""
calificaciones 	= {"calculo":10, "dibujo":5, "etica":4}
print("materia con mejor promedio: ", max(calificaciones.values()))

"""
Crear una lista la cual almacene 10 números positivos ingresados por el usuario, 
mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor
"""
contador 	= 0
notas 		= []
while contador < 10:
	
	nota = int(input("Ingrese nota:"))

	if nota < 0:
		print("Numero debe ser positivo")
		break

	notas.append(nota)
	contador+=1
else:
	print(notas)
	print(sum(notas))
	print(sum(notas)/len(notas))
	print(max(notas))
	print(min(notas))

"""
Mostrar en pantalla la palabra que más se repita junto con la cantidad de veces que lo hace 
del capituló número uno de Frankenstein
"""

cadenaPalabras = """esto es un texto de prueba
, buscar otro texto
"""

#Remplazar caracteres
cadenaPalabras = cadenaPalabras.replace("r\n", "")
cadenaPalabras = cadenaPalabras.replace("-", "")
cadenaPalabras = cadenaPalabras.replace("¿", "")
cadenaPalabras = cadenaPalabras.replace("?", "")
cadenaPalabras = cadenaPalabras.replace("(", "")
cadenaPalabras = cadenaPalabras.replace(")", "")
cadenaPalabras = cadenaPalabras.replace("\"\"", "")
cadenaPalabras = cadenaPalabras.replace("¡", "")
cadenaPalabras = cadenaPalabras.replace("!", "")
cadenaPalabras = cadenaPalabras.replace(",", "")
cadenaPalabras = cadenaPalabras.replace(".", "")
cadenaPalabras = cadenaPalabras.replace(";", "")
cadenaPalabras = cadenaPalabras.replace(":", "")

listaPalabras 	= cadenaPalabras.split()

frecuenciaPalab = []
for palabra in listaPalabras:
	frecuenciaPalab.append(listaPalabras.count(palabra))
#frecuenciaPalab = [listaPalabras.count(w) for w in listaPalabras] # a list comprehension

dicfrec = dict(list(zip(listaPalabras, frecuenciaPalab)))
aux 	= []
for key in dicfrec:
	aux.append((dicfrec[key], key))

aux.sort()
aux.reverse()
print(max(aux))

"""
Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo
"""
text 	= input("Ingrese una frase: ")
text 	= text.replace(' ', '')
#falta quitar acentos pero esta bien
cadena 	= text.lower()

if list(cadena) == list(cadena[::-1]):
	print("Es palíndromo")
else:
	print("No es palíndromo")

"""
Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el abecedario y mostrar 
el nuevo string en pantalla. (Los espacios no se remplazan). 
Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
"""
frase 			= input("Ingrese una frase: ")
palabras 		= frase.lower().split()
abecedario_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","y","z"]
resultado 		= ""
aux_abecedario 	= []

for indice in range(len(abecedario_list)):
	aux_abecedario.append([abecedario_list[indice], indice +1])
abecedario = dict(aux_abecedario)

for palabra  in palabras:
	for letra in palabra:
		existe = letra in abecedario_list
		if existe:
			resultado += str(abecedario[letra])
	resultado+=" "

print(resultado)

"""
Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario.
"""
frase 			= input("Ingrese una frase: ")
palabras 		= frase.lower().split()
vocales 		= ["a","e","i","o","u"]

contador = 0
for palabra  in palabras:
	for letra in palabra:
		existe = letra in vocales
		if existe:
			contador += 1

print(palabras)
print("Cantidad de vocales", contador)

"""
Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.
"""
frases 			= input("Ingrese una frase: ")
print(frases)
frases 			= frases.lower().split()

list_vocales 	= ["a","e","i","o","u"]
letras          = []
vocales 		= []
frecuencia      = []

for frase in frases:
	for letra in frase:
		if letra in list_vocales:
			if letra not in vocales:
				vocales.append(letra)
		letras.append(letra)

for vocal in vocales:
	frecuencia.append(letras.count(vocal))

print(list(zip(vocales,frecuencia)))

"""
Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla
"""
frases 			= input("Ingrese una frase: ")
print(frases)
frases 			= frases.lower().split()

list_vocales 	= ["a","e","i","o","u"]
letras          = []
no_vocales 		= []
frecuencia      = []

for frase in frases:
	for letra in frase:
		if letra not in list_vocales:
			if letra not in no_vocales:
				no_vocales.append(letra)
		letras.append(letra)

for no_vocal in no_vocales:
	frecuencia.append(letras.count(no_vocal))

resultado = ''.join(no_vocales)
print(resultado)

"""
Listar todos los números pares del 0 al 100
"""
for numero in range(0,101):
	if numero%2 == 0:
		print(numero)