texto = "   curso de Python 3, Python básico   "

resultado = texto.strip()
resultado = resultado.upper()

print(resultado.isupper())
print(resultado.islower())
print(resultado)

curso = "Python"
version = "3"

resultado = "Curso de %s %s" %(curso, version)
print(resultado)

resultado = "Curso de {a} {b}".format(b=version, a=curso)
print(resultado)