def suma(parametro_requerido,*args):
  total = 0
  print(parametro_requerido)
  for valor in args:
    total+=valor
  return total

resultado = suma("Este es un argumento requerido",10, 20, 30, 40, 50, 60, 70)
print(resultado)

def usuarios_autenticados(**kwargs):
  return kwargs

info_usuario = usuarios_autenticados(nombre='cristian', apellido='vidal', edad=28)
print(info_usuario)

def listado_nombres(*args):
	return args
nombres = listado_nombres('cristian','daniel','gustavo')
print(nombres)

def combinacion(requerido, *args, **kwargs):
  print(requerido)
  print(args)
  print(kwargs)

combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)
