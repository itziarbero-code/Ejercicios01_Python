#PY0003
asistentes = []

while True:
    nombre = input("Introduce un nombre (o 'fin' para terminar): ")

    if nombre.lower() == "fin":
        break

    asistentes.append(nombre)

print("Lista inicial:", asistentes)


consulta = input("¿Qué nombre quieres consultar? ")

print(f'count("{consulta}") = {asistentes.count(consulta)}')


if consulta in asistentes:
    print(f'index("{consulta}") = {asistentes.index(consulta)}')
    asistentes.remove(consulta)
    print(f'Tras remove("{consulta}"): {asistentes}')
else:
    print(f'El nombre "{consulta}" no está en la lista.')


vip = input("Introduce el nombre del asistente VIP: ")

asistentes.insert(0, vip)

print("Lista final:", asistentes)