
def centigrados_a_farhenheit(grados):
	return grados * 1.8 + 32
funcion_variable = centigrados_a_farhenheit
resultado	= funcion_variable(32)
#print(resultado)

"""
Las funciones Lamda son simplemente una forma rápida de definir una función 
(como cualquier otra en Python) 
y usualmente son usadas cuando se hacen filtrados en listas o para aplicar un mapeo a todos los elementos de una lista, 
o como función callback (un ejemplo clásico sería cuando se usa la función sort para 
definir el criterio de ordenamiento).
"""
mi_funcion = lambda grados=0 : grados * 1.8 + 32
resultado = mi_funcion(32)
print(resultado)

sin_parametros = lambda : True
print(sin_parametros)

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2
print(con_valores(1))

con_asterisco = lambda *args : args[0]
print(con_asterisco('hola','adios'))

con_doble_asterisco = lambda **kwargs : kwargs['valor_dos']
print(con_doble_asterisco(valor_uno='vidal', valor_dos='muñoz'))

#con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)