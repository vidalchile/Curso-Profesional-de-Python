diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}

#Buscar llave en el diccionario
resultado = "z" in diccionario
print(resultado)

resultado = diccionario.get("z", "la llave no existe")
print(resultado)

resultado = diccionario.setdefault("z", {})
print(resultado)

print(diccionario)