

def es_par_o_impar(numero):
    """
    Esta función recibe un número entero y determina si es par o impar.
    """
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

def main():
    try:
        numero = int(input("Ingresa un número entero: "))
        resultado = es_par_o_impar(numero)
        print(resultado)
    except ValueError:
        print("Por favor, ingresa un valor numérico entero válido.")


if __name__ == "__main__":
    main()