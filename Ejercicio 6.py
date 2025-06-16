import random

lista = [random.randint(1, 100) for _ in range(20)]
print(lista)

numero = int(input("Ingrese el número a buscar: "))

if numero in lista:
    posicion = lista.index(numero)
    print("El número está en la posición:", posicion)
else:
    print("Número no encontrado")