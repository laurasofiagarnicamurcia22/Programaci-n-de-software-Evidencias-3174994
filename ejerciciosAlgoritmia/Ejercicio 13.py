import random

lista = [random.randint(1, 100) for _ in range(20)]

def menu():
    print("\nMENÚ DE OPCIONES:")
    print("1. Buscar número y mostrar posición")
    print("2. Contar cuántas veces aparece un número")
    print("3. Mostrar número mayor y cuántas veces aparece")
    print("4. Verificar si un número aparece más veces que el mayor")
    print("5. Calcular la media de todos los números")
    print("6. Calcular la media entre el mayor y el menor")
    print("7. Mostrar lista invertida")
    print("0. Salir")

while True:
    print("\nLista actual:")
    print(lista)
    
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese el número a buscar: "))
        if numero in lista:
            print("Encontrado en la posición:", lista.index(numero))
        else:
            print("Número no encontrado")
    
    elif opcion == "2":
        numero = int(input("Ingrese el número a contar: "))
        cantidad = lista.count(numero)
        print("Aparece", cantidad, "veces")

    elif opcion == "3":
        mayor = max(lista)
        veces = lista.count(mayor)
        print("El número mayor es:", mayor)
        print("Aparece", veces, "veces")

    elif opcion == "4":
        numero = int(input("Ingrese un número: "))
        mayor = max(lista)
        if lista.count(numero) > lista.count(mayor):
            print(True)
        else:
            print(False)

    elif opcion == "5":
        media = sum(lista) / len(lista)
        print("Media:", media)

    elif opcion == "6":
        mayor = max(lista)
        menor = min(lista)
        media = (mayor + menor) / 2
        print("Media entre mayor y menor:", media)

    elif opcion == "7":
        lista_invertida = lista[::-1]
        print("Lista invertida:")
        print(lista_invertida)

    elif opcion == "0":
        print("Fin del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")