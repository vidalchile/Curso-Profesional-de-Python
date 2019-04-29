mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
print(list(mensaje))

#Cantidad de veces que existe una palabra en un string
resultado = mensaje.count("un");
print(resultado);

#Validar si existe una palabra en un string (booleano)
resultado = "longitud" in mensaje;
print(resultado)

#Buscar la posicion de la primera letra de la palabra buscada un string
resultado = mensaje.find("texto")
print(resultado)

#Extraer texto del string mensaje
resultado = mensaje[resultado: resultado + len("texto")]
print(resultado)

resultado = mensaje.startswith("Es");
print(resultado)

resultado = mensaje.endswith("a")
print(resultado)