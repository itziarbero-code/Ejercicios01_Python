lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

combinaciones = [
    (a, b)
    for a in lista1
    for b in lista2
    if (a + b) % 2 == 0
]

print(combinaciones)