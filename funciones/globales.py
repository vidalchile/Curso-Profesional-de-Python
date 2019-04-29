animal = 'León' #Es una variable global

def mostrar_animal():
  global animal
  animal = 'Ballena' #variables locales
  print(animal)

def mostrar_animal_2():
  global animal
  animal = 'Perro' #variables locales
  print(animal)

mostrar_animal()
mostrar_animal_2()
print(animal)