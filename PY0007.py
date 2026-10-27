
calificaciones = [
    {"alumno": "Ana", "modulo": "Programación", "nota": 7.5},
    {"alumno": "Ana", "modulo": "Sistemas", "nota": 8.0},
    {"alumno": "Luis", "modulo": "Sistemas", "nota": 6.0},
    {"alumno": "Marta", "modulo": "Programación", "nota": 9.0},
    {"alumno": "Ana", "modulo": "Programación", "nota": 8.5},
    {"alumno": "Luis", "modulo": "Programación", "nota": 4.0},
    {"alumno": "Marta", "modulo": "Sistemas", "nota": 4.5},
    {"alumno": "Luis", "modulo": "Sistemas", "nota": 7.0}
]

alumnos = {}

for registro in calificaciones:
    nombre = registro["alumno"]
    modulo = registro["modulo"]
    nota = registro["nota"]

    alumnos.setdefault(nombre, {}).setdefault(modulo, []).append(nota)

print("1. ESTRUCTURA DE ALUMNOS")
print(alumnos)


medias_alumnos = {}

for nombre, modulos in alumnos.items():
    mejores_notas = [
        max(notas)
        for notas in modulos.values()
        if notas
    ]

    if mejores_notas:
        medias_alumnos[nombre] = (
            sum(mejores_notas) / len(mejores_notas)
        )

print("\n2. MEDIA DE CADA ALUMNO")
print(medias_alumnos)



modulos_alumnos = {}

for nombre, modulos in alumnos.items():
    for modulo, notas in modulos.items():
        if notas:
            nota_maxima = max(notas)

            modulos_alumnos.setdefault(modulo, {})[
                nombre
            ] = nota_maxima

print("\n3. NOTA MÁXIMA POR ALUMNO Y MÓDULO")
print(modulos_alumnos)


from copy import deepcopy

correcciones = {
    "Ana": {"Programación": +0.75},
    "Luis": {"Sistemas": -0.5}
}

alumnos_corregidos = deepcopy(alumnos)

for nombre, modulos_correccion in correcciones.items():
    for modulo, cambio in modulos_correccion.items():

        notas = (
            alumnos_corregidos
            .get(nombre, {})
            .get(modulo, [])
        )

        if notas:
            notas[-1] += cambio
            print(
                f"Corrección aplicada a {nombre}, {modulo}: "
                f"última nota = {notas[-1]}"
            )
        else:
            print(
                f"No se puede corregir: {nombre} "
                f"no tiene notas en {modulo}."
            )

print("\n5. ALUMNOS CON CORRECCIONES")
print(alumnos_corregidos)



def eliminar_nota(alumnos, nombre, modulo, indice):
    if nombre not in alumnos:
        print("Error: el alumno no existe.")
        return None

    if modulo not in alumnos[nombre]:
        print("Error: el alumno no tiene ese módulo.")
        return None

    notas = alumnos[nombre][modulo]

    if indice < 0 or indice >= len(notas):
        print("Error: índice de nota no válido.")
        return None

    nota_eliminada = notas.pop(indice)

    if not notas:
        alumnos[nombre].pop(modulo)

    if not alumnos[nombre]:
        alumnos.pop(nombre)

    return nota_eliminada


eliminada = eliminar_nota(
    alumnos_corregidos,
    "Ana",
    "Programación",
    0
)

if eliminada is not None:
    print("\n6. NOTA ELIMINADA")
    print("Nota eliminada:", eliminada)

print("Estructura después de eliminar la nota:")
print(alumnos_corregidos)
