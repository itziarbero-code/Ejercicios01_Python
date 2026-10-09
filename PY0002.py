#PY0002
lista = [1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4]

for i in range(len(lista)):
    precio = lista[i]

    if precio < 0:
        continue

    if i % 2 == 0:
        descuento = 0.10
    else:
        descuento = 0.20
    
    nuevo_precio = precio * (1 - descuento)

    print(f"indice_lista={i}, precio_antes={precio:.2f}, precio_después={nuevo_precio:.2f}")

    lista[i] = nuevo_precio

print("Lista actualizada:", lista)