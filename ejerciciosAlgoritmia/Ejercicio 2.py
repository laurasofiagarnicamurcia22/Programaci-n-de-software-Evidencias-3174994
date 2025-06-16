def calcular_suma_hasta_n(n):
    """
    Calcula la suma de los números desde 1 hasta n.
    """
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def main():
    try:
        n = int(input("Ingresa un número entero positivo: "))
        if n < 1:
            print("El número debe ser mayor o igual a 1.")
        else:
            resultado = calcular_suma_hasta_n(n)
            print(f"La suma de 1 + 2 + ... + {n} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")


if __name__ == "__main__":
    main()