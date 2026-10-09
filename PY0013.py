import time

cadena = input("Introduce una cadena de texto: ")
caracter1 = input("Introduce el carácter que quieres sustituir: ")
caracter2 = input("Introduce el carácter nuevo: ")

if len(caracter1) != 1 or len(caracter2) != 1:
    print("Error: debes introducir un solo carácter.")
    time.sleep(3)
    exit()

print("\tCadena modificada:")

cadena = cadena.replace(caracter1, caracter2, 2)

print(cadena)