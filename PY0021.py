numeros = [10, 15, 100, 40, 35, 353, 400, 40, 500, 420, 340, 115]

resultado = sorted([n for n in numeros if n != 40 and n <= 339])

print(resultado)