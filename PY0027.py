
#PY0027
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

administradores = {"Juan", "Marta"}

administradores.discard("Juan")

administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(f"{usuario}: Es administrador")
    else:
        print(f"{usuario}: No es administrador")
