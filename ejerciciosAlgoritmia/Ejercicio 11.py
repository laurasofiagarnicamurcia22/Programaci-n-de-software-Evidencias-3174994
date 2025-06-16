import random

lista_numeros = []
print("Generando 20 números aleatorios entre 1 y 100...")
for i in range(20):
    numero_aleatorio = random.randint(1, 100)
    lista_numeros.append(numero_aleatorio)

print("Lista generada de 20 números aleatorios:")
print(lista_numeros)

numero_mayor = lista_numeros[0]  
for numero in lista_numeros:
    if numero > numero_mayor:
        numero_mayor = numero


numero_menor = lista_numeros[0] 
for numero in lista_numeros:
    if numero < numero_menor:
        numero_menor = numero


print("Número mayor encontrado en la lista:", numero_mayor)
print("Número menor encontrado en la lista:", numero_menor)

media_mayor_menor = (numero_mayor + numero_menor) / 2

print("La media entre el número mayor y el número menor es:", media_mayor_menor)