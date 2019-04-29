#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime
import math

"""
Ejercicio 1
Dado de los valores ingresados por el usuario (base, altura) 
calcular y mostrar en pantalla el área de un triángulo
"""
base 		= int(input("Ingresar base del triangulo:\n"))
altura 		= int(input("Ingresar altura del triangulo:\n"))
resultado 	= input("¿Deseas saber el area del del triangulo? (ok/no)\n") == "ok"
area 		= 1/2 * (base * altura)
print("Base del triangulo", base)
print("altura del triangulo", altura)
print("area del triangulo", area)

"""
Ejercicio 2
Convertir la cantidad de dólares ingresados por un usuario
a pesos colombianos y mostrar el resultado en pantalla.
"""
peso_colombiano	= 3.185
cantidad_dolar 	= int(input("Ingresar cantidad de dolares: "))
resultado 		= cantidad_dolar * peso_colombiano
print("Resultado pesos colombianos: ",resultado)

"""
Ejercicio 3
Convertir los grados centígrados ingresados por un usuario 
a grados Fahrenheit y mostrar el resultado en pantalla
(23 °C × 9/5) + 32 = 73,4 °F
"""
gc = int(input("Ingresar grados centígramos: "))
resultado = (gc * 9/5) + 32;
print("Grados Fahrenheit", resultado)

"""
Ejercicio 4
Mostrar en pantalla la cantidad de segundos que tiene un lustro.
"""
resultado 	= 5 * 365 * 24 * 60 * 60;
print("Cantidad de segundos que tiene un lustro", resultado)

"""
Ejercicio 5 (Pendiente)
Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte 
y mostrar el resultado en pantalla
"""

"""
Ejercicio 6 (Pendiente)
Calcular el número de vueltas que da una llanta en 1 km,  
dado que el diámetro de la llanta es de 50 cm, mostrar el resultado en pantalla.
"""

"""
Ejercicio 7
Calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros 
de altura cuando el ángulo que forman los rayos del sol con el suelo es de 22º.
"""
longitud_sombra = 20 / math.tan(math.radians(22))
print("La longitud de la sombra es: ", longitud_sombra)

"""
Ejercicio 8
Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma
"""
usuario_a 	= int(input("Ingresar edad usuario A: "))
usuario_b 	= int(input("Ingresar edad usuario B: ")) == usuario_a
print(usuario_b)

"""
Ejercicio 9
Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario
"""
#Día actual
today = date.today()
#Fecha actual
now = datetime.now()
ano = int(input("Introduzca su año de nacimiento: "))
mes = int(input("Introduzca su mes de nacimiento: "))
dia = int(input("Introduzca su día de nacimiento: "))
fecha_nacimiento = date(ano, mes, dia)
diff_dias  = (today - fecha_nacimiento).days
print("Cantidad de meses transcurridos entre %s y hoy es: %s" % (fecha_nacimiento, diff_dias / 30))



