diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7, 'h':8}
print(len(diccionario))
print(diccionario)

del diccionario["a"]
print(len(diccionario))
print(diccionario)

valor = diccionario.pop("b")
print(len(diccionario))
print(diccionario)
print(valor)

diccionario.clear()
print(len(diccionario))
print(diccionario)