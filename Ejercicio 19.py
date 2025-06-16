entrada = input("Ingrese un número entero: ")

if entrada.lstrip("-").isdigit():
    if entrada.startswith("-"):
        numero_sin_signo = entrada[1:]  
    else:
        numero_sin_signo = entrada

    cantidad_cifras = len(numero_sin_signo)

    print("El número tiene", cantidad_cifras, "cifras.")
else:
    print("Entrada inválida. Por favor ingrese un número entero válido.")