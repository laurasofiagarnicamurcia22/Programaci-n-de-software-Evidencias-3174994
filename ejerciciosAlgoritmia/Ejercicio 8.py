import random

lista = [random.randint(1, 100) for _ in range(20)]
print(lista)

mayor = max(lista)
contador = lista.count(mayor)

print("El número mayor es:", mayor)
print("Aparece", contador, "veces")