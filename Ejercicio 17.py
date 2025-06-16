aprendices = ["Arias", "Bohorquez", "Cruz", "Dominguez", "Forero", "Garnica", "Jaramillo" , "Luque", "Moreno", "Zabala"]

print("Lista original:")
print(aprendices)

nuevo = input("Ingrese el apellido del nuevo aprendiz: ")
aprendices.append(nuevo)
aprendices.sort()

print("Lista actualizada:")
print(aprendices)