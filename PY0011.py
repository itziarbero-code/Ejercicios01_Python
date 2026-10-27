listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

resultado = [numero for sublista in listas for numero in sublista]

print(resultado)