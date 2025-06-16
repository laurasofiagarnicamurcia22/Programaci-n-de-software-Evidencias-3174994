nit = int(input("Ingrese el número de NIT: "))

letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
          "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

indice = nit % 23
print(letras[indice])