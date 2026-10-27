
import time

cadena = input("Introduce una cadena de texto: ")
caracter1 = input("Introduce el carácter que quieres sustituir: ")
caracter2 = input("Introduce el carácter nuevo: ")

datos = {}

if len(caracter1) != 1 or len(caracter2) != 1:
    print("Error: debes introducir un solo carácter.")
    time.sleep(3)
    exit()

try:
    ocurrencias = int(input("¿Cuántas ocurrencias quieres sustituir?: "))

    if ocurrencias < 0:
        print("Error: el número de ocurrencias no puede ser negativo.")
        time.sleep(3)
        exit()

    datos[caracter1] = ocurrencias

except ValueError:
    print("Error: debes introducir un número entero.")
    time.sleep(3)
    exit()

print("\tCadena modificada:")

cadena = cadena.replace(caracter1, caracter2, datos[caracter1])

print(cadena)
