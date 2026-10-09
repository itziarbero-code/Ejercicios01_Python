#PY0043
cadena = input("Introduce una cadena de texto: ")
cadena = cadena.lower()

caracteres = []

for letra in cadena:
    if letra != " " and letra not in caracteres:
        caracteres.append(letra)

for letra in caracteres:
    contador = 0
    
    for caracter in cadena:
        if caracter == letra:
            contador += 1

    print(letra, ":", contador)