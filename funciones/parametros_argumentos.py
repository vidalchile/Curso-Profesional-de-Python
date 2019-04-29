def crear_usuario(nombre='', apellido='', edad=10):
	return {
		'nombre' : nombre,
		'apellido': apellido,
		'nombre_completo' : "{} {}".format(nombre, apellido),
		'edad': edad
	}

nuevo_usuario = crear_usuario('Daniel', 'Vidal', 23)
print(nuevo_usuario["nombre"])
print(nuevo_usuario["apellido"])
print(nuevo_usuario["edad"])

codi = crear_usuario(edad=11, apellido='Facilito', nombre='Codi')
print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])