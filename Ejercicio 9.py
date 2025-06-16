import random

lista = [random.randint(1, 100) for _ in range(20)]
print(lista)

numero = int(input("Ingrese un número: "))

mayor = max(lista)
veces_mayor = lista.count(mayor)
veces_numero = lista.count(numero)

print(veces_numero > veces_mayor)