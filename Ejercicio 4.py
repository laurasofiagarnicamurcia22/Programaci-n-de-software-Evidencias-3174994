inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma_pares = 0

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero

print("La suma de los números pares es:", suma_pares)