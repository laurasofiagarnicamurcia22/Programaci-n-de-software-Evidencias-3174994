import random

# Generar 3 dígitos aleatorios diferentes entre 0 y 9
digitos_objetivo = random.sample(range(10), 3)

intentos = 0
encontrado = False

print("Bienvenido al juego Rojo - Amarillo - Verde")
print("Debes adivinar 3 dígitos diferentes en el orden correcto (entre 0 y 9).")

while not encontrado:
    intentos += 1
    entrada = input(f"\nIntento #{intentos} - Ingrese 3 dígitos separados por espacios: ")

    # Convertir entrada a lista de enteros
    partes = entrada.strip().split()
    
    if len(partes) != 3 or not all(p.isdigit() for p in partes):
        print("Entrada inválida. Debes ingresar exactamente 3 números.")
        continue

    intento = [int(p) for p in partes]

    if len(set(intento)) != 3:
        print("Los dígitos deben ser distintos entre sí.")
        continue

    # Crear la pista
    pista = []
    for i in range(3):
        if intento[i] == digitos_objetivo[i]:
            pista.append("verde")
        elif intento[i] in digitos_objetivo:
            pista.append("amarillo")
        else:
            pista.append("rojo")

    print("Pista:", " - ".join(pista))

    if pista == ["verde", "verde", "verde"]:
        encontrado = True
        print(f"\nFelicidades. Adivinaste los dígitos en {intentos} intentos.")
        print("La combinación era:", digitos_objetivo)