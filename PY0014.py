#PY0014
try:
    num1 = int( input("Introduce un número") )
    num2 = int( input("Introduce otro número") )
    num3 = int( input("Introduce otro número") )

    media = num1 * 0.15 + num2 * 0.35 + num3 * 0.50

    print(f"La media ponderada es: {media:.2f}");

except ValueError:
    print("Error: debes introducir números.")