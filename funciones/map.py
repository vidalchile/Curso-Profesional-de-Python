def cuadrado(numero):
	return numero * numero

lista 		= [1,2,3,4,5]
resultado 	= map(cuadrado, lista)
resultado2 	= map(lambda numero: numero * numero , lista)

lista_resultado 	= list(resultado)
lista_resultado2 	= list(resultado2)

print(lista_resultado)
print(lista_resultado2)
