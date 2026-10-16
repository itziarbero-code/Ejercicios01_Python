#PY0025

paises = ["España", "Argentina", "Perú"]
intentos = 0
salir = False

def mostrar_menu():
    print("MENÚ. Elija una de las siguientes opciones marcando su número:")
    print("1. Imprimir alfabéticamente en orden ascendente")
    print("2. Imprimir alfabéticamente en orden descendente")
    print("3. Añadir País")
    print("4. Eliminar País")
    print("5. Salir")


def mostrar_paises(lista):
    print(lista)
    print("\n")


def anadir_pais(lista):
    pais = input("Introduce el país que quieres añadir: ").strip().capitalize()

    if pais == "":
        print("Error: no se puede añadir un país vacío.")
    elif pais in lista:
        print("Error: ese país ya está en la lista.")
    elif len(lista) >= 6:
        print("Error: no se pueden añadir más de 6 países.")
    else:
        lista.append(pais)
        print("País añadido correctamente.")
        mostrar_paises(lista)


def eliminar_pais(lista):
    pais = input("Introduce el país que quieres eliminar: ").strip().capitalize()

    if pais == "":
        print("Error: no has introducido ningún país.")
    elif pais in lista:
        lista.remove(pais)
        print("País eliminado correctamente.")
        mostrar_paises(lista)
    else:
        print("Error: el país no está en la lista.")


while not salir:
    correcto = False

    try:
        mostrar_menu()
        opcion = int(input("Elige una opción (1-5): "))
        intentos += 1

        if opcion < 1 or opcion > 5:
            raise ValueError("La opción debe estar entre 1 y 5.")

        if opcion == 1:
            print("Países en orden ascendente:")
            mostrar_paises(sorted(paises))

        elif opcion == 2:
            print("Países en orden descendente:")
            mostrar_paises(sorted(paises, reverse=True))

        elif opcion == 3:
            anadir_pais(paises)

        elif opcion == 4:
            eliminar_pais(paises)

        elif opcion == 5:
            salir = True

        correcto = True

    except ValueError as error:
        intentos += 1
        print("Error: introduce un número entero entre 1 y 5.")
        # El menú se volverá a mostrar en la siguiente iteración.

    except Exception as error:
        print("Se ha producido un error:", error)

    finally:
        print("Número de ejecuciones del menú:", intentos)

    if correcto and not salir:
        print("#" * 70)
        print("\n\n")

if salir:
    print("¡Gracias por utilizar el programa!")
    print("Número total de intentos:", intentos)
    print("¡Hasta pronto!")
