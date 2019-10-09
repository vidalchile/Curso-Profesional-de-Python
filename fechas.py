#Es necesario importar las depencendias necesarias
from datetime import date, datetime, timedelta

#OBTENER LA FECHA ACTUAL
#Día actual
today = date.today()
#Fecha actual
now = datetime.now()
print(today)
print(now)

#ATRIBUTOS
#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))
#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

#NUEVA FECHA
#Los argumentos serán: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos.
new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)
print('Nueva fecha {}'.format(new_date))

#OPERACIONES
#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

#Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")

#FORMATO DE FECHAS
#%d Día
#%m Mes
#%Y Año
#%H Hora
#%M Minutos
#%S segundos
now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

#  Definir una función que me permita obtener un formato mucho más amigable.
def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)
    return messsage

now = datetime.now()
print(current_date_format(now))

#EJERCICIO
#calcular la forma en que transcurrió un determinado periodo de 
# tiempo entre una hora y otra, 
# tengo por ejemplo entrada y salida de empleados de la oficina con 
# entrada supongamos que a las 10:00 am y con salida a las 5:30 pm

#Definimos una entrada por default : 10:00 AM 
entrada = datetime(2019, 3, 15, 9, 30, 00, 00000)
print(entrada)

#Definimos una salida por default : 5:00 PM
salida = datetime(2019, 3, 15, 19, 00, 00, 00000)
print(salida)

#Obtenemos los segundos transcurridos entre ambas fechas
tiempo_transcurrido = salida - entrada
segundos_transcurridos = tiempo_transcurrido.seconds

#Convertimos los segundos a horas String
horas_transcurridas = str(timedelta(seconds=segundos_transcurridos))
print(horas_transcurridas)