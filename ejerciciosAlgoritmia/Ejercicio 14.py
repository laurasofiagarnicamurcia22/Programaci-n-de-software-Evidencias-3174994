texto = input("Ingrese un texto: ")
palabras = texto.split()

cantidad_palabras = len(palabras)
tamano_mayor = max(len(palabra) for palabra in palabras)

print(cantidad_palabras)
print(tamano_mayor)