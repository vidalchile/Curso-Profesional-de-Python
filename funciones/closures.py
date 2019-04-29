def mostrar_mensaje(mensaje):
	
	mensaje = mensaje.title() #local
	 
	def mostrar():
	  print('Resultado:',mensaje)
	
	return mostrar

nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()

def comenzar_play_list(lista):
	
	def reproducir():
		nonlocal lista
		lista = [1,2,3]
		for val in lista:
	  		print(val)
	
	return reproducir

lista = ['track 1', 'track 2', 'track 3', 'track 4']
otra_funcion = comenzar_play_list(lista);
otra_funcion()