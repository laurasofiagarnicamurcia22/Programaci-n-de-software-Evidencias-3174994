valor = int(input("Ingrese el valor a cobrar: "))
monto = int(input("Ingrese el monto entregado: "))

cambio = monto - valor

if cambio < 0:
    print("Falta dinero")
else:
    monedas = [1000, 500, 200, 100, 50]
    for moneda in monedas:
        cantidad = cambio // moneda
        cambio %= moneda
        print(moneda, cantidad)