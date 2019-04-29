"""
Un yield puede entenderse como una especie de return que no retorna realmente del todo

yield funciona similar a un return pero la diferencia importante es que conserva la iteración.

Hay veces que es preferible que una función vaya devolviendo los resultados a medida que los obtiene 
en vez de devolverlos todos juntos al final de su ejecución. 
Ése es el cometido de yield, el de retornar un valor de una secuencia de valores.
"""

def tabla_multiplicar(numero, maximo = 10):
	for posicion in range(1, maximo+1):
		yield numero * posicion, numero, posicion	

tabla_multiplicar7 = tabla_multiplicar(7)
for resultado, numero, posicion in tabla_multiplicar7:
	print(numero, "*", posicion, "=", resultado)

print("\r\n")

tabla_multiplicar9 = tabla_multiplicar(9)
for resultado, numero, posicion in tabla_multiplicar9:
	print(numero, "*", posicion, "=", resultado)

print("\r\n")

def contador(max):
	n=1
	while n <= max:
		yield n
		n=n+1

contad1 = contador(5)
for i in contad1:
    print("contad1 valor: ",str(i))

print("\r\n")

contad2 = contador(10)
for i in contad2:
    print("contad2 valor: ",str(i))