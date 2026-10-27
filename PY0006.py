inventario_inicial = {
    'CUS001': 12,
    'CUS002': 5,
    'CUS003': 0
}

ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']

reposiciones = {
    'CUS002': 10,
    'CUS004': 7
}


inventario = inventario_inicial.copy()

avisos = []


for codigo in ventas:
    if codigo not in inventario:
        inventario.setdefault(codigo, 0)
        avisos.append(
            f"Aviso: el producto {codigo} no existía en el inventario."
        )

    inventario[codigo] = inventario.get(codigo, 0) - 1


print("AVISOS DE VENTAS")
for aviso in avisos:
    print(aviso)


for codigo, cantidad in reposiciones.items():
    inventario[codigo] = inventario.get(codigo, 0) + cantidad


print("\nINFORME DEL INVENTARIO")
print("Número de referencias:", len(inventario))
print("Unidades totales:", sum(inventario.values()))

print("\nInventario antes de eliminar productos:")
print(inventario)


claves_a_borrar = [
    codigo
    for codigo, stock in inventario.items()
    if stock <= 0
]

for codigo in claves_a_borrar:
    inventario.pop(codigo)

print("\nInventario después de eliminar productos sin stock:")
print(inventario)


codigo_consulta = input(
    "\nIntroduce el código del producto que deseas consultar: "
).strip().upper()

if codigo_consulta in inventario:
    print(
        f"Stock de {codigo_consulta}: "
        f"{inventario[codigo_consulta]} unidades"
    )
else:
    print("No existe")


del inventario

print("\nEl diccionario de trabajo ha sido eliminado.")
print("El inventario original sigue conservado:")
print(inventario_inicial)
