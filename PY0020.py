#PY0020
while True:
    operacion = input(
        "Introduce una operación (+, -, *, /) o escribe 'salir' para terminar: "
    )

    if operacion == "salir":
        print("Programa terminado.")
        break

    if operacion not in ("+", "-", "*", "/"):
        print("Error: operación no válida.")
        continue

    try:
        num1 = int(input("Introduce un número entero: "))
        num2 = int(input("Introduce otro número entero: "))

        match operacion:
            case "+":
                resultado = num1 + num2

            case "-":
                resultado = num1 - num2

            case "*":
                resultado = num1 * num2

            case "/":
                if num2 == 0:
                    print("Error: no se puede dividir entre cero.")
                    continue

                resultado = num1 / num2

        print(f"La solución a la operación es: {resultado:.2f}")

    except ValueError:
        print("Error: debes introducir números enteros.")
