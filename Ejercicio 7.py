import random

lista = [random.randint(1, 100) for _ in range(20)]
print(lista)

numero = int(input("Ingrese el número a buscar: "))
contador = lista.count(numero)

if contador > 0:
    print("El número aparece", contador, "veces")
else:
    print("Número no encontrado")