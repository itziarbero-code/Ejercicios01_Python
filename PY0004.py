#PY0004 
# Crear el menú base
menu_base = ["Ensalada", "Sopa", "Pasta"]

# Hacer una copia independiente
menu_hoy = menu_base.copy()

# Añadir los especiales al menú de hoy
menu_hoy.extend(["Pescado", "Postre"])

# Retirar el último plato añadido por error
menu_hoy.pop()

# Eliminar "Sopa" si está en la lista
if "Sopa" in menu_hoy:
    menu_hoy.remove("Sopa")

# Escoger una posición y eliminar su elemento
menu_hoy.pop(1)

# Mostrar el menú al revés
print("Menú al revés:", menu_hoy[::-1])

# Vaciar la lista base original
menu_base.clear()

# Demostrar que menu_hoy no se ha visto afectada
print("Menú base:", menu_base)
print("Menú de hoy:", menu_hoy)