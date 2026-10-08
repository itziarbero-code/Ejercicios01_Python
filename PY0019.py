#PY0019
while True:
  try:
    numero = int(input("Introduce un número entero: "))

    if numero % 2 == 0:
      print(f"El número {numero} es PAR.")
    else:
      print(f"El número {numero} es IMPAR.")
      break

  except ValueError:
    print("Por favor, introduce un número entero válido.")