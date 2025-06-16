numeros = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numeros.sort(reverse=True)

for numero in numeros:
    print(numero)