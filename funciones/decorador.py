#a, b, c
#a(b) -> c

"""
def funcion_a(funcion_b):

	def funcion_c():
		print("Podemos agregar codigo antes")
		funcion_b()
		print("Podemos agregar codigo despues")
	
	return funcion_c

@funcion_a #Decorador
def funcion_a_decorar():
	print("Este es una función a decorar")

funcion_a_decorar()
"""

def debug(f):
	def new_function(*args, **kwargs):
		print(f"Function {f.__name__}() called!")
		return f(*args, **kwargs)
	return new_function

@debug
def add(a,b):
	return a + b

@debug
def neg(n):
	return n * -1

print(add(2,4))
print(neg(2))