#PY0015
matriz = [
   [1, 1, 1, 3],
   [2, 2, 2, 7],
   [3, 3, 3, 9],
   [4, 4, 4, 13] ]

for fila in matriz:
    fila[3] = sum(fila[0:3:1])

print(matriz)