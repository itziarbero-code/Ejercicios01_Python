
inscritos = {"Ana", "Luis", "Marta", "Pedro"}

print("Inscritos iniciales:", inscritos)

while True:
    nombre = input("Introduce un nombre (o 'fin' para terminar): ")

    if nombre.lower() == "fin":
        break

    # Comprobar que no esté vacío ni tenga espacios al principio o al final
    if not nombre or nombre != nombre.strip():
        print("Error: el nombre no puede estar vacío ni tener espacios al principio o al final.")
        continue

    inscritos.add(nombre)
    print(f"{nombre} ha sido añadido.")


nombres_lote = input(
    "Introduce varios nombres separados por comas: "
)

nuevo_lote = {
    nombre.strip()
    for nombre in nombres_lote.split(",")
    if nombre.strip() != ""
}

inscritos.update(nuevo_lote)

print("Inscritos después del lote:", inscritos)


copia_inscritos = inscritos.copy()
print("Copia del conjunto:", copia_inscritos)


nombre_baja = input("Introduce el nombre que deseas dar de baja: ")

try:
    inscritos.remove(nombre_baja)
    print(f"{nombre_baja} ha sido dado de baja.")
except KeyError:
    print(f"Error: {nombre_baja} no está inscrito en el taller.")


nombre_consulta = input("¿Qué persona quieres consultar?: ")

if nombre_consulta in inscritos:
    print(f"{nombre_consulta} está inscrito/a en el taller.")
else:
    print(f"{nombre_consulta} no está inscrito/a en el taller.")


grupo_personas = {"Ana", "Carlos", "Lucía", "Pedro"}

print("Grupo de personas:", grupo_personas)

coincidencias = grupo_personas & inscritos

if coincidencias:
    print("Personas del grupo inscritas en el taller:", coincidencias)
else:
    print("Ninguna persona del grupo está inscrita en el taller.")


print("Número total de inscritos:", len(inscritos))
print("Lista de inscritos ordenada:", sorted(inscritos))
