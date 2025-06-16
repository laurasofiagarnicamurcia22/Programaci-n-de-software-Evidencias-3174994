import random

lista = [random.randint(1, 100) for _ in range(20)]
print(lista)

media = sum(lista) / len(lista)
print(media)