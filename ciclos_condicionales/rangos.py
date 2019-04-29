#esta es la primera forma en la que podemos usar la funcion range.
for valor in range(100):
	print(valor)

"""Esta es la segunda forma en la cual podemos usar la función range con esta forma podemos 
escojer desde donde comienza nuestra lista"""
for valor in range(5,11):
	print(valor)

""" 
Esta es la tercera forma en la que podemos utilizar la función range
"""
lista = [1,2,3,4,5,6]

for indice in range(len(lista)):
	print(indice, lista[indice])

lista = [1,2,3,4,5,6]

for indice, valor in enumerate(lista):
	print(indice, valor)

""" 
En esta nueva forma le podemos especificar al indice 
desde donde buscamos que inicie
"""
for indice, valor in enumerate(lista, 20):
	print(indice, valor)
